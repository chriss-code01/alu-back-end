
#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""

import csv
import json
import os
import sys
from urllib.parse import urlencode
from urllib.request import urlopen


def fetch_data(url):
    """Fetch JSON data from a URL."""
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Export an employee's TODO list to CSV."""
    if len(sys.argv) != 2:
        return

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = fetch_data("{}/users/{}".format(base_url, user_id))
    params = urlencode({"userId": user_id})
    todos = fetch_data("{}/todos?{}".format(base_url, params))

    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "{}.csv".format(user_id)
    )

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()

