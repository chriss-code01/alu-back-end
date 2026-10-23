
#!/usr/bin/python3
"""Gather an employee's TODO list progress from an API."""

import json
import sys
from urllib.request import urlopen
from urllib.parse import urlencode


def fetch_data(url):
    """Fetch JSON data from a URL."""
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Print an employee's completed tasks and progress."""
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

    employee_name = user.get("name")
    done_tasks = [
        task for task in todos if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), len(todos)
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()

