#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

def get_employee_todo_list(employee_id):
    """base_url: the link of the database"""
    base_url = 'https://jsonplaceholder.typicode.com'
    """user_url: leads to employee details"""
    user_url = f'{base_url}/users/{employee_id}'
    """todos_url: leads to tasks"""
    todos_url = f'{base_url}/todos?user_Id={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_date = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_date['name']
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task['completed'])

        print(f'Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):')
        for task in todos_data:
            if task['completed']:
                print(f'\t{task["title"]}')

    except requests.RequestException as e:
        print(f'Error fetching data: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 script.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
