from TaskModule.Task import Task
from TaskModule.TaskReminder import Reminder
from TaskModule.ReminderList import ReminderList
import datetime as dt

def main():
    t1 = Task("task1", dt.datetime.today(), "task1_description")
    t2 = Task("task2", dt.datetime.today() + dt.timedelta(1), "task1_description")
    r1 = Reminder(t1, t1.due_date - dt.timedelta(10))
    r2 = Reminder(t2, t2.due_date - dt.timedelta(4))
    rl = ReminderList()
    s = rl.check_reminders()
    print(s)
main()