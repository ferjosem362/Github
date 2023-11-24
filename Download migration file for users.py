import requests
import os
import tarfile

# Retrieve token from environment variable
github_token = os.getenv("GITHUB_TOKEN")

# Ensure the token is available
if not github_token:
    raise ValueError("GitHub token not found in environment variables")

# Replace 'MIGRATION_ID' with the actual migration ID
migration_id = "MIGRATION_ID"
url = f"https://api.github.com/user/migrations/{migration_id}/archive"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(url, headers=headers, allow_redirects=False)

# Handle response based on the status code
if response.status_code == 302:
    download_url = response.headers.get('Location')
    if download_url:
        archive_response = requests.get(download_url)
        archive_file_path = 'migration_archive.tar.gz'
        with open(archive_file_path, 'wb') as file:
            file.write(archive_response.content)
        print("Migration archive downloaded successfully.")

        # Extracting the tar.gz file
        with tarfile.open(archive_file_path, "r:gz") as tar:
            tar.extractall(path="migration_archive")
        print("Migration archive extracted successfully.")
    else:
        print("Download URL not found in the response.")
elif response.status_code == 304:
    print("Not modified. No new data to return.")
elif response.status_code == 401:
    print("Authentication required.")
elif response.status_code == 403:
    print("Forbidden. Access is not allowed.")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
