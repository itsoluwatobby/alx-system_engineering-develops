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


users_url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(users_url)

try:
    if response.status_code == 200:
        users = response.json()
        todo_url = 'https://jsonplaceholder.typicode.com/todos'

        res = requests.get(todo_url)
        todos = res.json()
        users_todos = []

        # index = 1
        for user in users:
            print(user)
            for todo in todos:
                if todo['userId'] == user['id']:
                    users_todos[user['id']].append(todo)

        print(user_todos)
        # json_format = '{{"{}": ['.format(user['id'])
        # for todo in users_todos[:-1]:
        #    json_format += '{{"task": "{}", "completed": {}, "username": "{}"}}, '\
        #    .format(todo['title'],str(todo['completed']).lower(),user['username'])

        # l_todo = users_todos[-1]
        # last_val = '{{"task": "{}", "completed": {}, "username": "{}"}}'\
        #        .format(l_todo['title'],str(l_todo['completed']).lower(),user['username'])

        # json_format += '{}]}}'.format(last_val)

        # with open('todo_all_employees.json', 'w') as file:
        #    file.write(json_format)
    else:
        raise Exception("Error: {}".format(response.status_code))
except Exception as e:
    print(e)
