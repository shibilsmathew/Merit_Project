# Function to display tasks
class TaskManager:
    def display_tasks(self):
        tasks_data = []
        for index, task in enumerate(self.tasks, 1):
            tasks_data.append([index, task.title, task.status, task.time_taken, task.expected_finish])
        headers = ["", "Task", "Status", "Time Taken", "Finished at"]
        print(tabulate(tasks_data, headers=headers, tablefmt="grid"))
