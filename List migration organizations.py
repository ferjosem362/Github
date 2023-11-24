import requests
import os

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

url = "https://api.github.com/orgs/SKY-UK/migrations"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(url, headers=headers)

# Basic error handling
if response.status_code == 200:
    print("Successfully retrieved migrations.")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.json())
