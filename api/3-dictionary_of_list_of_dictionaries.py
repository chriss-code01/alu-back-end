#!/usr/bin/python3
"""Export all employees' TODO tasks to a JSON file."""

import json
import sys
from urllib.request import urlopen


def fetch_data(url):
    """Fetch JSON data from a URL."""
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Export every employee's tasks into one JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        users = fetch_data("{}/users".format(base_url))
        todos = fetch_data("{}/todos".format(base_url))
    except Exception as error:
        print("Error fetching data: {}".format(error), file=sys.stderr)
        return

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[str(user_id)] = []

        for task in todos:
            if task.get("userId") == user_id:
                all_tasks[str(user_id)].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    main()
