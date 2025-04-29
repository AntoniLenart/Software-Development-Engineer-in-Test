import requests


class APIClient:
    def get_user_data(self, user_id: int):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("API request failed")


class UserService:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_username(self, user_id: int) -> str:
        user_data = self.api_client.get_user_data(user_id)
        return user_data["name"].upper()
