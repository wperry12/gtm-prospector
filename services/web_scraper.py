# /services/web_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_article_text(url: str) -> str | None:
    """
    Scrapes the text content from a given URL.

    Args:
        url: The URL of the article to scrape.

    Returns:
        The scraped text as a string, or None if an error occurs.
    """
    if not url:
        return None
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])
        return article_text[:4000] # Truncate for API limits
    except requests.RequestException as e:
        print(f"Could not scrape {url}: {e}")
        return None