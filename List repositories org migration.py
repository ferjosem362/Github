import requests
import os

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

# Replace 'MIGRATION_ID' with the actual migration ID
url = "https://api.github.com/orgs/SKY-UK/migrations/MIGRATION_ID/repositories"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(url, headers=headers)

# Error handling and processing each repository
if response.status_code == 200:
    repositories = response.json()
    for repo in repositories:
               print(repo.get('name', 'No name provided'))
elif response.status_code == 404:
    print("Resource not found.")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
