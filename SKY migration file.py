import csv
import requests
import os
import json
# Read repository names from the CSV file
with open('migration.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    repositories = [row[0] for row in csv_reader]

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

# Read repository names from the CSV file
with open('migration.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    repositories = [row[0] for row in csv_reader]

url = "https://api.github.com/orgs/SKY-UK/migrations"
payload = {
    "repositories": repositories,
    "lock_repositories": True,
    "exclude_metadata": False,
    "exclude_git_data": True,
    "exclude_attachments": False,
    "exclude_releases": False,
    "exclude_owner_projects": False,
    "org_metadata_only": False
}
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

# Error handling
if response.status_code == 201:
    print("Migration created successfully.")
    print(response.json())
elif response.status_code in [404, 422]:
    print(f"Error {response.status_code}: {response.json().get('message', 'No specific message provided')}")
else:
    print(f"Unexpected error: {response.status_code}")
    print(response.json())

