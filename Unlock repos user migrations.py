import requests
import os
import json

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

# Load user data from JSON file (this is the current json file I've got from the SKY-UK organization)
with open('export-sky-uk-1700732645.json', 'r') as file:
    users = json.load(file)

# Headers
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Iterating over each user and their repositories
for user in users:
    migration_id = user['migration_id']  # Replace with actual key for migration ID
    for repo_name in user['repositories']:  # Replace with actual key for repositories
        url = f"https://api.github.com/user/migrations/{migration_id}/repos/{repo_name}/lock"
        response = requests.delete(url, headers=headers)

        # Error handling
        if response.status_code == 204:
            print(f"Repository {repo_name} for user {user['name']} unlocked successfully.")  # Replace 'name' with actual user identifier key
        elif response.status_code in [304, 401, 403, 404]:
            print(f"Error unlocking {repo_name} for user {user['name']}: {response.status_code} - {response.reason}")
        else:
            print(f"Unexpected error unlocking {repo_name} for user {user['name']}: {response.status_code}")
            print(response.json())
