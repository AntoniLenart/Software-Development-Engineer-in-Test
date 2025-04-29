class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, email):
        if username in self.data:
            raise ValueError("Username already exists")
        self.data[username] = email
        return True

    def get_user(self, username):
        return self.data.get(username)

    def delete_user(self, username):
        if username not in self.data:
            raise ValueError("User not found")
        del self.data[username]
        return True
