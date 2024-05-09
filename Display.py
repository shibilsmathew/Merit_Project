def list_tasks(self):
    for index, task in enumerate(self.tasks, 1):
        print(f"{index}. {task}")

