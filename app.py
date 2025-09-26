# /app.py
"""Main Flask application for the GTM Prospector tool.

Handles web routes, orchestrates service calls, and renders the UI.
"""
import os
import csv
import markdown
from flask import Flask, request, render_template, redirect, url_for

# Local application imports
import config
from services import google_search, web_scraper, lusha_api, gemini_ai
from utils.connections import find_internal_connection, process_uploaded_csv

# --- App Setup ---
app = Flask(__name__)
config.check_api_keys()

# Ensure the data directory for CSV uploads exists on startup.
if not os.path.exists('data'):
    os.makedirs('data')

@app.route('/', methods=['GET', 'POST'])
def interactive_analysis():
    """Main route for the application, handles both GET and POST requests.

    On GET, it displays the search page. On POST, it orchestrates the
    entire analysis pipeline: fetching news, generating AI summaries and GTM
    plans, finding contacts, and enriching them with internal connection
    data before rendering the results.

    Returns:
        A rendered HTML template with the analysis data.
    """
    # view_data holds all variables passed to the Jinja2 template.
    view_data = {
        "company_name": request.form.get('company_name', '').strip(),
        "scorecard_html": "",
        "briefing_html": "",
        "gtm_strategy_html": "",
        "prioritized_prospects": [],
        "sources": []
    }

    # Only run the analysis pipeline on a POST request with a company name.
    if request.method == 'POST' and 'analyze_button' in request.form and view_data["company_name"]:
        company_name = view_data["company_name"]
        is_demo = company_name.lower() == config.DEMO_COMPANY_NAME

        # 1. Fetch and scrape news articles.
        if is_demo:
            view_data["sources"] = google_search.find_company_news_demo(company_name)
            scraped_articles_text = ["Demo content used, no scraping needed."]
        else:
            view_data["sources"] = google_search.find_company_news(company_name)
            scraped_articles_text = [
                f"Title: {item['title']}\nContent: {text}"
                for item in view_data["sources"]
                if (text := web_scraper.scrape_article_text(item.get('link')))
            ]
        
        full_text_for_prompt = "\n\n---\n\n".join(scraped_articles_text)

        # 2. Generate AI strategy summary from scraped text.
        ai_summary_md = (gemini_ai.summarize_ai_strategy_demo(company_name, full_text_for_prompt)
                         if is_demo else gemini_ai.summarize_ai_strategy(company_name, full_text_for_prompt))
        
        parts = ai_summary_md.split('---', 1)
        view_data["scorecard_html"] = markdown.markdown(parts[0].strip() if parts else "")
        view_data["briefing_html"] = markdown.markdown(parts[1].strip() if len(parts) > 1 else "")
        
        # 3. Find employee contacts via Lusha API.
        lusha_contacts = (lusha_api.find_employees_with_lusha_demo(company_name)
                          if is_demo else lusha_api.find_employees_with_lusha(company_name))

        # 4. Enrich contacts with internal connection data from the local CSV.
        connections_data = []
        try:
            with open(config.CONNECTIONS_CSV_PATH, mode='r', newline='', encoding='utf-8') as f:
                connections_data = list(csv.DictReader(f))
        except FileNotFoundError:
            print("ℹ️  linkedin_connections.csv not found. No connections will be checked.")

        enriched_employees = [
            {**contact, **find_internal_connection(contact['name'], connections_data)}
            for contact in lusha_contacts
        ]

        # 5. Generate a Go-To-Market strategy based on all gathered intelligence.
        if enriched_employees:
            gtm_data = (gemini_ai.generate_gtm_strategy_demo(company_name, ai_summary_md, enriched_employees)
                        if is_demo else gemini_ai.generate_gtm_strategy(company_name, ai_summary_md, enriched_employees))
            
            # If GTM data is successfully generated, unpack it for the template.
            if gtm_data:
                view_data["prioritized_prospects"] = gtm_data.get('prioritized_prospects', [])
                strategy_text = gtm_data.get('outreach_strategy', "No strategy provided.")
                messages = gtm_data.get('message_templates', [])
                
                # Build GTM HTML from markdown components.
                gtm_html_parts = [markdown.markdown(strategy_text)]
                if messages:
                    gtm_html_parts.append("<h3>Message Templates</h3>")
                    for msg in messages:
                        gtm_html_parts.append(f"<h4>For: {msg.get('target_role', 'N/A')} via {msg.get('channel', 'Email')}</h4>")
                        formatted_message = markdown.markdown(msg.get('message', ''))
                        gtm_html_parts.append(f"<div class='message-box'>{formatted_message}</div>")
                view_data["gtm_strategy_html"] = "".join(gtm_html_parts)
            else:
                # Fallback if the GTM generation fails.
                view_data["prioritized_prospects"] = enriched_employees
                view_data["gtm_strategy_html"] = "<p><em>Error: Could not generate the GTM strategy.</em></p>"
        else:
             view_data["gtm_strategy_html"] = "<p><em>No employees found to generate a GTM strategy.</em></p>"

    return render_template("index.html", **view_data)


@app.route('/upload', methods=['POST'])
def upload_csv():
    """Handles POST requests for uploading LinkedIn connections CSV.

    Processes the uploaded file and appends the connection data to the
    persistent CSV file defined in the config.

    Returns:
        A redirect to the main page on success, or a tuple (error_message, status_code) on failure.
    """
    salesperson = request.form.get('salesperson_name')
    file = request.files.get('csv_file')
    
    if not file or not salesperson:
        return "Missing file or salesperson name.", 400
    
    try:
        process_uploaded_csv(file, salesperson, config.CONNECTIONS_CSV_PATH)
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return f"An unexpected error occurred: {e}", 500
        
    return redirect(url_for('interactive_analysis'))


# Run the Flask development server.
if __name__ == '__main__':
    app.run(debug=True, port=5001)