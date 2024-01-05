#!/usr/bin/python3
"""export data receieved from api in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    users_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(users_id)).json()
    user_name = user.get("username")
    todo = requests.get(url + "todos", params={"userId": users_id}).json()

    """opens a json file and writes to it according to user id"""
    with open("{}.json".format(users_id), "w") as file_json:
        json.dump({users_id: [{"task": h.get("title"),
                               "completed": h.get("completed"),
                               "username": user_name} for h in todo]},
                  file_json)
