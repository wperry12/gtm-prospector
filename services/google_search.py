# /services/google_search.py
"""Client for the Google Custom Search API to find company news."""
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from typing import List, Dict, Any
from .demo_data import DUMMY_CBA_NEWS
from config import GOOGLE_API_KEY, GOOGLE_CSE_ID

def find_company_news(company_name: str) -> List[Dict[str, Any]]:
    """Fetches news articles about a company's AI strategy.

    Args:
        company_name: The company to search for.

    Returns:
        A list of search result items from the Google API, or an empty
        list if the call fails or keys are not configured.
    """
    if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
        print("Google Search API credentials not configured. Skipping news search.")
        return []
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        query = f'"{company_name}" artificial intelligence strategy OR AI implementation'
        res = service.cse().list(q=query, cx=GOOGLE_CSE_ID, num=5).execute()
        return res.get('items', [])
    except HttpError as e:
        print(f"Google Search API Error: {e}")
        return []

def find_company_news_demo(company_name: str) -> List[Dict[str, Any]]:
    """Returns a static list of news articles for testing.

    Bypasses the API to provide a predictable response for demos.

    Args:
        company_name: The company name (used for logging).

    Returns:
        A hardcoded list of dicts representing news articles.
    """
    print(f"Using DUMMY News Data for '{company_name}'...")
    return DUMMY_CBA_NEWS