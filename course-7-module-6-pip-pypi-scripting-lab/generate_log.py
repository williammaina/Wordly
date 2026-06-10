#!/usr/bin/env python3
"""
Root-level Automation Script
Requirement: Fetches data via 'requests' and writes a log summary using File I/O.
"""

import sys
from datetime import datetime
import requests

# Target public API
API_URL = "https://jsonplaceholder.typicode.com/posts/1"

def fetch_data():
    """Fetches data from a public API using the third-party requests package."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # Ensures we handle HTTP errors (404, 500, etc.)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        return {}

def main():
    print("Starting automation tool...")
    
    # 1. Fetch the data using external dependency
    post = fetch_data()
    
    if not post:
        print("Automation failed: No data retrieved.", file=sys.stderr)
        sys.exit(1)
        
    # 2. Extract structured data
    post_id = post.get("id", "N/A")
    title = post.get("title", "No title found")
    body = post.get("body", "No content found")
    
    # 3. Define the exact log format and root-level filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    log_data = [
        f"--- Automation Log Summary ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---",
        "User Action: Data Fetch Execution",
        f"Fetched Post ID: {post_id}",
        f"Fetched Post Title: {title}",
        f"Content Snippet: {body[:60]}...",
        "------------------------------------------------"
    ]
    
    # 4. Write results to output file using File I/O
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for entry in log_data:
                file.write(f"{entry}\n")
        print(f"Log successfully written to {filename}")
    except IOError as e:
        print(f"File I/O Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()