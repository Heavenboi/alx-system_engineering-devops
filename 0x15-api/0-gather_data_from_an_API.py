#!/usr/bin/python3
import requests
import sys


def get_user_todo():
    """
    a function that return employee's name
    and number of task they completed
    """

    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
        return

    employee_id = int(sys.argv[1])
    api_url_users = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    user = requests.get(api_url_users).json()

    api_url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos = requests.get(api_url_todos).json()

    tasks = sum(1 for todo in todos if todo["completed"])
    task_names = "\n".join(todo["title"]
                           for todo in todos if todo["completed"])

    print(f"Employee {user['name']} is done with tasks({tasks}/20):\n{task_names}")


if __name__ == "__main__":
    get_user_todo()
