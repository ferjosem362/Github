import requests
import os

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

url = "https://api.github.com/orgs/SKY-UK/migrations/migration_id/archive"  # migration_id is the actual code (integer) for the migration
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}"
}

response = requests.get(url, headers=headers, allow_redirects=True)

# Error handling
if response.status_code == 302:
    # Redirect to the URL provided in the Location header to download the file
    download_url = response.headers.get('Location')
    if download_url:
        print(f"Redirecting to download URL: {download_url}")
        
    else:
        print("Download URL not found in the response.")
elif response.status_code == 404:
    print("Resource not found.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
