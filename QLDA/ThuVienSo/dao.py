import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "users.json")

def auth_login(username : str, password ):
    with open(file_path, "r", encoding="utf-8") as f:
        users = json.load(f)

        for u in users :
            if u["username"] == username and u["password"] == password :
                return True

        return False

if __name__ == "__main__" :
    print(auth_login("user1", 123))