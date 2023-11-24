import requests
import os
import csv

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

# Replace 'MIGRATION_ID' with the actual migration ID
migration_id = "MIGRATION_ID"
base_url = "https://api.github.com/orgs/SKY-UK/migrations/{}/repos".format(migration_id)
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Read repository names from the CSV file
with open('migration.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        repo_name = row[0]
        url = f"{base_url}/{repo_name}/lock"
        response = requests.delete(url, headers=headers)

        # Error handling for each repository
        if response.status_code == 204:
            print(f"Repository {repo_name} unlocked successfully.")
        elif response.status_code == 404:
            print(f"Resource not found for repository {repo_name}.")
        else:
            print(f"Error unlocking {repo_name}: {response.status_code}")
            print(response.json())
