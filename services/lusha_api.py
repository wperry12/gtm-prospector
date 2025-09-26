# /services/lusha_api.py
"""Client for the Lusha Prospecting API to find employee contacts."""
import requests
import json
from typing import List, Dict, Any
from .demo_data import DUMMY_CBA_LUSHA_PAYLOAD # Import dummy data
from config import LUSHA_API_KEY

def find_employees_with_lusha(company_name: str) -> List[Dict[str, Any]]:
    """Searches the Lusha API for senior-level contacts at a company.

    Results are de-duplicated and filtered to remove restricted contacts.

    Args:
        company_name: The company to search for.

    Returns:
        A list of unique contact dicts, each with name, role, and company.
        Returns an empty list on failure or if keys are not configured.
    """
    if not LUSHA_API_KEY:
        print("Lusha API key is not configured. Skipping search.")
        return []

    api_url = "https://api.lusha.com/prospecting/contact/search"
    headers = {'api_key': LUSHA_API_KEY, 'Content-Type': 'application/json'}
    # NOTE: Seniority 9 targets C-Suite, VPs, and Directors.
    payload = {
        "filters": {
            "contacts": {"include": {"seniority": [9]}},
            "companies": {"include": {"names": [company_name]}}
        }
    }
    # Use contact name as dict key to de-duplicate results.
    all_found_contacts = {}

    print(f"Running Lusha search for '{company_name}'...")
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()

        if data.get('data') and isinstance(data['data'], list):
            for contact in data['data']:
                name = contact.get("name", "N/A").strip()
                if name.lower() != 'restricted' and name != "N/A":
                    all_found_contacts[name] = {
                        'name': name,
                        'role': contact.get("jobTitle", "N/A").strip(),
                        'company': contact.get("companyName", "N/A").strip()
                    }
    except requests.RequestException as e:
        print(f"Error calling Lusha API: {e}")
        if e.response:
            print(f"API Error (Status {e.response.status_code}): {e.response.text}")
    except Exception as e:
        print(f"An unexpected error occurred during Lusha search: {e}")

    final_list = list(all_found_contacts.values())
    print(f"Lusha API Success: Found {len(final_list)} unique contacts.")
    return final_list

def find_employees_with_lusha_demo(company_name: str) -> List[Dict[str, Any]]:
    """Returns a static list of Lusha contacts for testing.

    Bypasses the API to provide a predictable response for demos and unit tests,
    avoiding network latency and API quota usage.

    Args:
        company_name: The company name (used for logging).

    Returns:
        A hardcoded list of contact dicts.
    """
    print(f"Using DUMMY Lusha data for '{company_name}'...")
    all_found_contacts = {}
    if DUMMY_CBA_LUSHA_PAYLOAD.get("data"):
        for contact in DUMMY_CBA_LUSHA_PAYLOAD["data"]:
            name = contact.get("name", "N/A").strip()
            if name.lower() != 'restricted' and name != "N/A":
                all_found_contacts[name] = {
                    'name': name,
                    'role': contact.get("jobTitle", "N/A").strip(),
                    'company': contact.get("companyName", "N/A").strip()
                }
    final_list = list(all_found_contacts.values())
    print(f"Dummy Lusha Data: Processed {len(final_list)} contacts.")
    return final_list