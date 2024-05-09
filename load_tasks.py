import openpyxl

class TaskTracker:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            wb = openpyxl.load_workbook(self.file_name)
            ws = wb.active
            tasks = []
            for row in ws.iter_rows(values_only=True):
                tasks.append(Task(row[0], row[1], row[2]))
            wb.close()
            return tasks
        except FileNotFoundError:
            return []
