from TaskModule.Task import Task
from TaskModule.TaskList import TaskList
from TaskModule.TaskReminder import Reminder
from TaskModule.ReminderList import ReminderList
from TaskModule.TaskListView import TaskListView
from TaskModule.ReminderListView import ReminderListView
import datetime as dt

def main():
    t1 = Task("task1", dt.datetime.today(), "task1_description")
    t2 = Task("task2", dt.datetime.today() + dt.timedelta(1), "task2_description")
    t2 = Task("task3", dt.datetime.today() + dt.timedelta(1), "task1_description")

    rem_list = ReminderList()
    task_list = TaskList()
    task_view = TaskListView(task_list)
    task_list.add_task(t1)
    task_list.add_task(t2)
    rem_view = ReminderListView(rem_list)
    print("===TO DO LIST / REMINDER APP")
    while(True):
        printSelectionMenu()
        choice = input()
        while not choice.isnumeric() or int(choice) > 6 or int(choice) < 0:
            print("Please enter a valid number")
            choice = input()
        i_choice = int(choice)
        if i_choice == 0:
            print("Thank you for using this program!")
            return
        elif i_choice == 1:
            print(task_view.viewTasks())
        elif i_choice == 2:
            format = "%m-%d-%Y"
            name = input("Enter the name of your task: ")
            res = False
            date = None
            while not res:
                date = input ("Enter date in mm-dd-yyyy format: ")
                try:
                    res = dt.datetime.strptime(date, format)
                except ValueError:
                    res = False
            desc = input("Enter a description for this task: ")
            task_list.add_task(Task(name, res, desc))
        elif i_choice == 3:
            print(task_view.viewTasks())
            del_choice = input("Enter the ID of the task you'd like to delete: ")
            while not del_choice.isnumeric() or int(del_choice) >= len(task_list.tasks) or int(del_choice) < 0:
                print("Please enter a valid number")
                del_choice = input()
            task_list.remove_task_at_index(int(del_choice))
        elif i_choice == 4:
            print(task_view.viewTasks())
            t_choice = input("Enter the ID of the task you'd like to be reminded of: ")
            while not t_choice.isnumeric() or int(t_choice) >= len(task_list.tasks) or int(t_choice) < 0:
                print("Please enter a valid number")
                t_choice = input()
            format = "%m-%d-%Y"
            res = False
            date = None
            while not res:
                date = input ("Enter date of reminder in mm-dd-yyyy format: ")
                try:
                    res = dt.datetime.strptime(date, format)
                except ValueError:
                    res = False
            rem_list.add_reminder(Reminder(task_list.tasks[int(t_choice)], res))
        elif i_choice == 5:
            print(rem_view.viewReminders())
        elif i_choice == 6:
            print(task_view.viewTasks())
            t_choice = input("Enter the ID of the task you'd like to mark as done: ")
            while not t_choice.isnumeric() or int(t_choice) >= len(task_list.tasks) or int(t_choice) < 0:
                print("Please enter a valid number")
                t_choice = input()
            task_list.tasks[int(t_choice)].done = True
        print(rem_list.check_reminders())
        print("===============")



def printSelectionMenu():
    print("Enter a number corresponding to the option you'd like to perform")
    print("1. View your tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Add a reminder to a task")
    print("5. View reminders")
    print("6. Mark task as done")
    print("0. EXIT")
main()