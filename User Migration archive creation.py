import requests
import os
import json

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

# Load user data from JSON file
with open('export-sky-uk-1700732645.json', 'r') as file:
    user_data = json.load(file)

# Assuming user_data contains an array of users, each with a 'repositories' field
for user in user_data:
    url = "https://api.github.com/user/migrations"
    payload = {
        "repositories": user['repositories'],
        "lock_repositories": True,
        "exclude_metadata": False,
        "exclude_git_data": False,
        "exclude_attachments": False,
        "exclude_releases": False,
        "exclude_owner_projects": False,
        "org_metadata_only": False
    }
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.post(url, headers=headers, json=payload)

    # Handle response
    if response.status_code == 201:
        print(f"Migration archive created for user {user['name']}.")
    else:
        print(f"Error for user {user['name']}: {response.status_code}")
        print(response.json())
