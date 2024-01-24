#!/usr/bin/python3
"""export data receieved from api in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    users_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(users_id)).json()
    user_name = user.get("username")
    todo = requests.get(url + "todos", params={"userId": users_id}).json()

    """opens a csv file and writes to it according to user id"""
    with open("{}.csv".format(users_id), "w") as csvfile:
        """writer object created with each field in quotes"""
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        """csv file creatd with each row containing user id, user name,
        completed statuses, and title of task"""
        [writer.writerow([users_id, user_name, h.get("completed"),
                          h.get("title")]) for h in todo]
