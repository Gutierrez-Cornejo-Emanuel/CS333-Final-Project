from TaskModule.Task import Task
from TaskModule.TaskList import TaskList
from TaskModule.TaskReminder import Reminder
from TaskModule.ReminderList import ReminderList
from TaskModule.TaskListView import TaskListView
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
    print("===TO DO LIST / REMINDER APP")
    while(True):
        printSelectionMenu()
        choice = input()
        while not choice.isnumeric() or int(choice) > 5 or int(choice) < 0:
            print("Please enter a valid number")
            choice = input()
        i_choice = int(choice)
        if i_choice == 0:
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
                print(type(res))
            desc = input("Enter a description for this task: ")
            task_list.add_task(Task(name, date, desc))
        elif i_choice == 3:
            print(task_view.viewTasks())
            del_choice = input("Enter the ID of the task you'd like to delete: ")
            while not del_choice.isnumeric() or int(del_choice) >= len(task_list.tasks) or int(del_choice) < 0:
                print("Please enter a valid number")
                del_choice = input()
            task_list.remove_task_at_index(int(del_choice))
            




def printSelectionMenu():
    print("Enter a number corresponding to the option you'd like to perform")
    print("1. View your tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Add a reminder to a task")
    print("5. View reminders")
    print("0. EXIT")
main()