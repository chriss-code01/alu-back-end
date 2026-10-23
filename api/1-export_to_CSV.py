#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file."""
import csv
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

    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])
