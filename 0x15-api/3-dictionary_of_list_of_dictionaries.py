#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Export the result in JSON format

Requirements:
    * Records all tasks that are owned by this employee
    * Format must be: { "USER_ID": [ {"username": "USERNAME",
        "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS}, ... ],
        "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
        "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    * File name must be: todo_all_employees.json
"""

import requests


def todo_with_user(todo, user):
    """Returns the string concatenation of the todo and user"""
    return '{{"username": "{}", "task": "{}", "completed": {}}}'\
           .format(user.get('username'), todo.get('title'),
                   str(todo.get('completed')).lower())


def create_json_format(user, todos):
    """Returns the array string format of the employee todos"""
    user_todos = []

    for todo in todos:
        if todo.get('userId') == user.get('id'):
            user_todos.append(todo)

    json_ft = '"{}": ['.format(user.get('id'))
    for todo in user_todos[:-1]:
        json_ft += todo_with_user(todo, user) + ', '

    last_user_todo = todo_with_user(user_todos[-1], user)

    json_ft += '{}]'.format(last_user_todo)
    return json_ft


users_url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(users_url)

try:
    if response.status_code == 200:
        users = response.json()
        todo_url = 'https://jsonplaceholder.typicode.com/todos'

        res = requests.get(todo_url)
        todos = res.json()

        all_todos = '{'
        for user in users[:-1]:
            all_todos += create_json_format(user, todos) + ', '

        last_todo = create_json_format(users[-1], todos)
        all_todos += '{}}}'.format(last_todo)

        with open('todo_all_employees.json', 'w') as file:
            file.write(all_todos)
    else:
        raise Exception("Error: {}".format(response.status_code))
except Exception as e:
    print(e)
