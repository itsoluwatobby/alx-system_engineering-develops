#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Export the result in JSON format

Requirements:
    * Records all tasks that are owned by this employee
    * Format must be: { "USER_ID": [{"task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
      {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
      "username": "USERNAME"}, ... ]}
    * File name must be: USER_ID.json
"""

import requests
from sys import argv


user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
response = requests.get(user_url)

try:
    if response.status_code == 200:
        user = response.json()
        todo_url = 'https://jsonplaceholder.typicode.com/todos'

        res = requests.get(todo_url)
        todos = res.json()
        user_todos = []

        for todo in todos:
            if todo['userId'] == user['id']:
                user_todos.append(todo)

        json_format = '{{"{}": ['.format(user['id'])
        for todo in user_todos[:-1]:
            json_format += '{{"task": "{}", "completed": {}, "username": "{}"}}, '\
            .format(todo['title'], str(todo['completed']).lower(), user['username'])

        l_todo = user_todos[-1]
        last_val = '{{"task": "{}", "completed": {}, "username": "{}"}}'.format(
                    l_todo['title'], str(l_todo['completed']).lower(), user['username'])

        json_format += '{}]}}'.format(last_val)

        with open('{}.json'.format(user['id']), 'w') as file:
            file.write(json_format)
    else:
        raise Exception("Error: {}".format(response.status_code))
except Exception as e:
    print(e)
