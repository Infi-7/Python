import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import csv

# Load environment variables
load_dotenv()

# Validate and fetch site link
site_link = os.getenv("site_link")
if not site_link:
    raise ValueError("Missing 'site_link' in environment variables.")

# Initialize lists to store game names
games_names = []

# Fetch and parse data from the site
try:
    response = requests.get(site_link)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
except requests.exceptions.RequestException as e:
    raise SystemExit(f"Error fetching data from site: {e}")

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract data from <strong> tags (modify this based on actual HTML structure)
games_data = soup.find_all('strong')

games_names = [data.get_text() for data in games_data]

# Clean the extracted game names by removing the first word
final_list = [' '.join(name.split()[1:]).strip() for name in games_names]

# File path for CSV
file_path = "top_100_games.csv"

# Check if file exists and read existing data to avoid duplication
existing_data = []
if os.path.exists(file_path):
    with open(file_path, mode="r") as f:
        existing_data = [row[0] for row in csv.reader(f)]

# Filter out duplicate entries
new_data = [game for game in final_list[::-1] if game not in existing_data]

# Write new data to the CSV file
if new_data:
    with open(file_path, mode="a", newline="") as f:
        writer = csv.writer(f)
        for game in new_data:
            writer.writerow([game])

print(f"Successfully added {len(new_data)} new games to {file_path}.")
