class TaskListView:
    def __init__(self, task_list) -> None:
        self.task_list = task_list
    def viewTasks(self):
        s = f'{"ID":<3} || {"Name":<10} || {"Due Date":<30} || {"Description":<20} || {"Finished"}\n'
        for i, t in enumerate (self.task_list.tasks):
            s += (f'{i:<3} || {t.name:<10} || {str(t.due_date):<30} || {str(t.description):<20} || {"Done" if t.done else ""}\n' )
        return s