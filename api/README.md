# Employee TODO List API

## Description

This project uses the JSONPlaceholder REST API to retrieve employee information and TODO tasks. It demonstrates how to make HTTP requests, process JSON responses, and export data to text-based file formats using Python.

The scripts use Python's built-in `urllib` module, so the `requests` package is not required.

## Files

- `0-gather_data_from_an_API.py` — Displays an employee's TODO task progress.
- `1-export_to_CSV.py` — Exports an employee's tasks to a CSV file.
- `2-export_to_JSON.py` — Exports an employee's tasks to a JSON file.
- `3-dictionary_of_list_of_dictionaries.py` — Exports TODO tasks for all employees to a JSON file.

## Requirements

- Python 3
- Internet connection to access the JSONPlaceholder API

## Usage

Run the scripts from the `api` directory.

### 0. Display employee task progress

```bash
./0-gather_data_from_an_API.py EMPLOYEE_ID
```

### 1. Export employee tasks to CSV

```bash
./1-export_to_CSV.py EMPLOYEE_ID
```

The script creates a CSV file named `EMPLOYEE_ID.csv`.

### 2. Export employee tasks to JSON

```bash
./2-export_to_JSON.py EMPLOYEE_ID
```

The script creates a JSON file named `EMPLOYEE_ID.json`.

### 3. Export all employees' tasks to JSON

```bash
./3-dictionary_of_list_of_dictionaries.py
```

The script creates `todo_all_employees.json`.

Replace `EMPLOYEE_ID` with the numeric ID of the employee you want to query.

## API

The project uses the public JSONPlaceholder API:

https://jsonplaceholder.typicode.com/

## Author

ALU Back-End Python project.

