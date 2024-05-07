import datetime as dt
from .Task import Task
class Reminder:
    def __init__(self, task: Task, date: dt.date) -> None:
        self.task = task
        self.remind_date = date
        self.sent = False
    def checkReminder(self):
        if dt.datetime.now() >= self.remind_date and not self.sent:
            self.sent = True
            return str("Remember to do task " + self.task.name + " by " + str(self.task.due_date))
        return ""