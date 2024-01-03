#!/usr/bin/python3
import requests

print("Enter your ID:")
employee_id = input("")
api_url_users = 'https://jsonplaceholder.typicode.com/users/' + employee_id

user = requests.get(api_url_users).json()

tasks = 0
task_name = ""
for i in range((int(employee_id) - 1) * 20,
               (int(employee_id)) * 20, 1):
    api_url_todos = 'https://jsonplaceholder.typicode.com/todos/' + str(i+1)
    todos = requests.get(api_url_todos).json()
    if (todos["completed"]):
        tasks = tasks + 1
        task_name = task_name + todos["title"] + "\n"

print("Employee", user["name"],
      " is done with tasks ("+str(tasks)+"/20):\n" + task_name)
