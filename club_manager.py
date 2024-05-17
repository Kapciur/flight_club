import requests

URL  = "https://api.sheety.co/2c94ca9968b5819a555b5a2fd2884844/flightDeals/users"

class club_manager:
    def __init__(self):
        self.data = {}
    def get_user(self):
        response = requests.get(URL)
        self.data = response.json()["users"]
        return self.data
    def create_user(self):
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        email = input("What is your email address? ")
        email2 = input("Type your email address again: ")
        if email == email2:
            data = {
                "users": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                }
            }
            response = requests.post(URL, json=data)
            return response
