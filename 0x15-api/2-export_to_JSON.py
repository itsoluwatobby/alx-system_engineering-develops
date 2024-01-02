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


def todo_with_user(todo, user):
    """Returns the string concatenation of the todo and user"""
    return '{{"task": "{}", "completed": {}, "username": "{}"}}'\
           .format(todo.get('title'), str(todo.get('completed')).lower(),
                   user.get('username'))


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
            if todo.get('userId') == user.get('id'):
                user_todos.append(todo)

        json_ft = '{{"{}": ['.format(user.get('id'))
        for todo in user_todos[:-1]:
            json_ft += todo_with_user(todo, user) + ', '

        last_val = todo_with_user(user_todos[-1], user)
        json_ft += '{}]}}'.format(last_val)

        with open('{}.json'.format(user.get('id')), 'w') as file:
            file.write(json_ft)
    else:
        raise Exception("Error: {}".format(response.status_code))
except Exception as e:
    print(e)
