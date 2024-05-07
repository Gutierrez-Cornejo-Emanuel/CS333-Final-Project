class TaskList:
    def __init__(self) -> None:
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task_at_index(self, i):
        self.tasks.pop(i)
    def remove_finished_tasks(self):
        self.tasks = [t  for t in self.tasks if not t.done]