class TaskManager:
  def add_task(self, title):
  task = Task(title)
  self.tasks.append(task)
  self.save_tasks()
