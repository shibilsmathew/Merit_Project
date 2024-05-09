class TaskManager:
    def delete_task(self, task_number):
        del self.tasks[task_number - 1]
        self.save_tasks()
