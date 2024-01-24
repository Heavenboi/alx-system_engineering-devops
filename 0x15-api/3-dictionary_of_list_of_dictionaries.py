#!/usr/bin/python3
"""export data receieved from api in the JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    all_users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as file_json:
        json.dump({h.get("id"): [{"task": i.get("title"),
                                  "completed": i.get("completed"),
                                  "username": h.get("username")}
                                 for i in requests.get(url + "todos",
                                                       params={"userId":
                                                               h.get("id")})
                                 .json()] for h in all_users}, file_json)
