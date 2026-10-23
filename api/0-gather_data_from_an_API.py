#!/usr/bin/python3
"""Retrieve and display an employee's completed TODO tasks."""

import json
import sys
from urllib.parse import urlencode
from urllib.request import urlopen


def fetch_data(url):
    """Fetch JSON data from a URL."""
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Display an employee's completed tasks."""
    if len(sys.argv) != 2:
        return

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = fetch_data("{}/users/{}".format(base_url, user_id))
    params = urlencode({"userId": user_id})
    todos = fetch_data("{}/todos?{}".format(base_url, params))

    completed_tasks = [
        task for task in todos if task.get("completed")
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
            len(completed_tasks),
            len(todos)
        )
    )

    for task in completed_tasks:
        print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    main()
