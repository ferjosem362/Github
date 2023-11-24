import requests
import os

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

url = f"https://api.github.com/orgs/SKY-UK/migrations/001"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}"
}

response = requests.get(url, headers=headers)

# Error handling and status interpretation
if response.status_code == 200:
    migration_status = response.json().get('status', 'No status provided')
    if migration_status == "pending":
        print("Migration hasn't started yet.")
    elif migration_status == "exporting":
        print("Migration in progress.")
    elif migration_status == "exported":
        print("Migration finished successfully.")
    elif migration_status == "failed":
        print("Migration has failed.")
    else:
        print(f"Migration status: {migration_status}")
elif response.status_code == 404:
    print("Resource not found.")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
