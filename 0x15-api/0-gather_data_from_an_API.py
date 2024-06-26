#!/usr/bin/python3
""" This file describes a module that fetches and displasy a progress list
for given employee id using rest api """


import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    fetches and prints the TODO list progress of an employee

    Args:
        employee_id (int): The ID of the employee

    """

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user information")
        return

    user_data = user_response.json()

    # Fetch ToDo list information
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching TODO list information")
        return

    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get("name")
    if not employee_name:
        print(f"Employee name not found.")
        return

    # Calculate task completion
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get("completed")]
    number_of_tasks_done = len(done_tasks)

    # Display results
    print(f"Employee {employee_name} is done with tasks({number_of_tasks_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
