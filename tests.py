from TaskModule.Task import Task
from TaskModule.TaskList import TaskList
from TaskModule.TaskReminder import Reminder
from TaskModule.ReminderList import ReminderList
import unittest
import datetime as dt

class TaskListIntegrationTest(unittest.TestCase):
    def testAddTask(self):
        t1 = Task("task1", dt.datetime.today(), "task1_description")
        l = TaskList()
        self.assertEqual(len(l.tasks), 0)
        l.add_task(t1)
        self.assertEqual(len(l.tasks), 1)
        self.assertEqual(l.tasks[0], t1)
    def testRemoveTask(self):
        t1 = Task("task1", dt.datetime.today(), "task1_description")
        t2 = Task("task2", dt.datetime.today(), "task1_description")
        l = TaskList()
        l.add_task(t1)
        l.add_task(t2)
        l.remove_task_at_index(0)
        self.assertEqual(len(l.tasks), 1)
        self.assertEqual(l.tasks[0], t2)
    def testDeleteDone(self):
        t1 = Task("task1", dt.datetime.today(), "task1_description")
        t2 = Task("task2", dt.datetime.today(), "task1_description")
        t1.done = True
        l = TaskList()
        l.add_task(t1)
        l.add_task(t2)
        l.remove_finished_tasks()
        self.assertEqual(len(l.tasks), 1)
        self.assertEqual(l.tasks[0], t2)

class TaskReminderIntegrationTest(unittest.TestCase):
    def testReminderInteraction(self):
        t1 = Task("task1", dt.datetime.today(), "task1_description")
        r = Reminder(t1, t1.due_date - dt.timedelta(1))
        c = r.checkReminder()
        self.assertTrue(t1.name in c)
        self.assertTrue(str(t1.due_date) in c)
        r2 = Reminder(t1, t1.due_date + dt.timedelta(1))
        c2 = r.checkReminder()
        self.assertFalse(c2)

class ReminderListReminderIntegrationTest(unittest.TestCase):
    def testAddReminder(self):
        t1 = Task("task1", dt.datetime.today(), "task1_description")
        r = Reminder(t1, t1.due_date - dt.timedelta(1))
        rl = ReminderList()
        rl.add_reminder(r)
        self.assertTrue(len(rl.reminders) == 1)

    def testCheckReminders(self):
        t1 = Task("task1", dt.datetime.today(), "task1_description")
        t2 = Task("task2", dt.datetime.today() + dt.timedelta(1), "task1_description")
        r1 = Reminder(t1, t1.due_date - dt.timedelta(1))
        r2 = Reminder(t2, t2.due_date - dt.timedelta(4))
        rl = ReminderList()
        rl.add_reminder(r1)
        rl.add_reminder(r2)
        s = rl.check_reminders()
        self.assertTrue(t1.name in s)
        self.assertTrue(str(t1.due_date) in s)
        self.assertTrue(t2.name in s)
        self.assertTrue(str(t2.due_date) in s)



if __name__ == '__main__':
    unittest.main()