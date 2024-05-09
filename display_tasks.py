# Function to display tasks
def display_tasks():
    tasks = []
    for row in sheet.iter_rows(values_only=True):
        tasks.append(row)
    print(tabulate(tasks, headers=["Task", "Status"]))
