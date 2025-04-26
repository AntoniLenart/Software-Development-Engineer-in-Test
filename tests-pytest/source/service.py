import requests


def get_users():
    response = requests.get("http://jsonplaceholder.typicode.com/users")
    if response.status_code != 200:
        raise requests.HTTPError(f"Error: {response.status_code}")
    return response.json()


database = {
        1: "Alice",
        2: "Bob",
        3: "Charlie",
}


def get_user(user_id):
    """Fetches a user from the database."""
    if user_id not in database:
        raise ValueError(f"User with ID {user_id} does not exist.")
    return database[user_id]
