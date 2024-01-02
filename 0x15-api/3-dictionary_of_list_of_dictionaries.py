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
    return '{{"username": "{}", "task": "{}", "completed": {}}}'\
            .format(user['username'], todo['title'],
                    str(todo['completed']).lower())


def create_json_format(user, todos):
    user_todos = []

    for todo in todos:
        if todo['userId'] == user['id']:
            user_todos.append(todo)

    json_ft = '"{}": ['.format(user['id'])
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
