# /utils/connections.py
import csv
import os
from thefuzz import fuzz
from typing import List, Dict, Any, Tuple

def find_internal_connection(full_name: str, connections_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Checks if a given full name matches a name in the connections data.

    Args:
        full_name: The name of the person to check.
        connections_data: A list of dictionaries representing internal connections.

    Returns:
        A dictionary with connection status and the salesperson's name.
    """
    for row in connections_data:
        connection_full_name = f"{row.get('FirstName', '')} {row.get('LastName', '')}".strip()
        # Use a fuzziness ratio to account for slight name variations
        if connection_full_name and fuzz.ratio(full_name.lower(), connection_full_name.lower()) > 85:
            return {
                "connection_status": True,
                "connected_with": row.get('Salesperson', 'Unknown')
            }
    return {"connection_status": False, "connected_with": ""}

def process_uploaded_csv(file_storage, salesperson: str, csv_path: str):
    """
    Processes an uploaded CSV file of LinkedIn connections and appends it to the main connections file.

    Args:
        file_storage: The FileStorage object from Flask request.files.
        salesperson: The name of the salesperson uploading the file.
        csv_path: The path to the main connections CSV file.

    Raises:
        ValueError: If the CSV does not contain the required headers.
    """
    # Create the connections file with a header if it doesn't exist
    if not os.path.exists(csv_path):
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['FirstName', 'LastName', 'Company', 'Position', 'Salesperson'])

    # Decode the uploaded file stream
    stream = file_storage.stream.read().decode("utf-8-sig")
    csv_data = list(csv.reader(stream.splitlines()))

    # Find the header row in the uploaded LinkedIn CSV
    header_index = -1
    for i, row in enumerate(csv_data):
        if row and 'First Name' in row and 'Last Name' in row:
            header_index = i
            break
    
    if header_index == -1:
        raise ValueError("Could not find required headers ('First Name', 'Last Name') in CSV.")

    # Append the relevant data to our main connections file
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in csv_data[header_index + 1:]:
            # Basic validation for a standard LinkedIn connections export
            if not row or len(row) < 6:
                continue
            first_name, last_name, company, position = row[0], row[1], row[4], row[5]
            writer.writerow([first_name, last_name, company, position, salesperson])