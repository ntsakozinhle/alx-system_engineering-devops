#!/usr/bin/python3
"""
This file describes a module that fetches and exports a progress
list for given employee id to a JSON file.
"""


import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: tuple containing user data.
    """
    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user information")
        return None, None

    user_data = user_response.json()

    # Fetch ToDo list information
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching TODO list information")
        return user_data, None

    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_json(employee_id, user_data, todos_data):
    """
    Exports TODO list progress of an employee to a JSON file.

    Args:
        employee_id (int): the ID of the employee.
        user_data (dict): The employees's user data.
        todos_data (list): The list of TODO tasks.
    """
    filename = f"{employee_id}.json"
    tasks = [{"task": todo.get("title"), "completed": todo.get("completed"), "username": user_data.get("username")} for todo in todos_data]
    json_data = {str(employee_id): tasks}

    with open{filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    """
    Main block of the script. Validates command-line arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        user_data, todos_data = get_employee_todo_progress(employee_id)

        if user_data and todos_data:
            # Print the progress to the console
            employee_name = user_data.get("name")
            total_tasks = len(todos_data)
            done_tasks = [todo for todo in todos_data if todo.get("completed")]
            number_of_tasks_done = len(done_tasks)

            print(f"Employee {employee_name} is done with tasks({number_of_tasks_done}/{total_tasks}):")
            for task in done_tasks:
                print(f"\t {task.get('title')}")

            export_to_json(employee_id, user_data, todos_data)

    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
