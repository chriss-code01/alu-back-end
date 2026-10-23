#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""
import json
import sys
import urllib.request


def fetch_json(url):
    """Fetch a URL and return the parsed JSON."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = fetch_json("{}/users/{}".format(base_url, employee_id))
    todos = fetch_json("{}/todos?userId={}".format(base_url, employee_id))

    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
