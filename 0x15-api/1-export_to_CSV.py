#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Export the result in csv format

Requirements:
    * Records all tasks that are owned by this employee
    * Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    * File name must be: USER_ID.csv
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        print('Employee ID is required')
    else:
        user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
                   .format(argv[1])
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

                csv_format = ''
                for todo in user_todos:
                    csv_format += '"{}","{}","{}","{}"\n'.format(
                                    user.get('id'), user.get('username'),
                                    todo.get('completed'), todo.get('title'))

                with open('{}.csv'.format(user.get('id')), 'w') as file:
                    file.write(csv_format)
            else:
                raise Exception("Error: {}".format(response.status_code))
        except Exception as e:
            print(e)
