# Task Tracker
This Python program implements a simple task tracker using Excel files (.xlsx) as a storage medium. 

It allows users to add tasks, list tasks, mark tasks as complete, and delete tasks.

## Features
- **Add Task**: Users can add a new task by providing a title and description.
- **List Tasks**: Users can list all tasks along with their completion status.
- **Mark Task as Complete**: Users can mark a task as complete by specifying its number.
- **Delete Task**: Users can delete a task by specifying its number.
- **Quit**: Users can exit the task tracker.

## Dependencies
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/): A Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

## Usage
Install dependencies:
   ```bash
   pip install openpyxl
   python task_tracker.py
