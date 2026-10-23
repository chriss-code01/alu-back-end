#!/usr/bin/python3
"""Export an employee's TODO tasks to a JSON file."""

import json
import sys
from urllib.parse import urlencode
from urllib.request import urlopen


def fetch_data(url):
    """Fetch JSON data from a URL."""
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Write an employee's TODO tasks to a JSON file."""
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    base_url = "https://jsonplaceholder.typicode.com"

    try:
        user = fetch_data(
            "{}/users/{}".format(base_url, employee_id)
        )
        query = urlencode({"userId": employee_id})
        todos = fetch_data(
            "{}/todos?{}".format(base_url, query)
        )
    except Exception as error:
        print("Error fetching data: {}".format(error), file=sys.stderr)
        return

    if not isinstance(user, dict) or not user:
        return

    username = user.get("username")
    tasks = []

    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)

 
if __name__ == "__main__":
    main()

