# Continue from the previous code

# Assuming each user has a 'migration_id' field
for user in user_data:
    migration_id = user['migration_id']
    url = f"https://api.github.com/user/migrations/{migration_id}"
    response = requests.get(url, headers=headers)

    # Handle response
    if response.status_code == 200:
        print(f"User {user['name']} migration status: {response.json()}")
    else:
        print(f"Error for user {user['name']}: {response.status_code}")
        print(response.json())
