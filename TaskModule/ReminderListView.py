class ReminderListView:
    def __init__(self, reminder_list) -> None:
        self.reminder_list = reminder_list
    def viewReminders(self):
        s = f'{"ID":<3} || {"Task":<10} || {"Due Date":<30} || {"Reminder Date":<30} || {"Sent"}\n'
        for i, r in enumerate (self.reminder_list.reminders):
            s += (f'{i:<3} || {r.task.name:<10} || {str(r.task.due_date):<30} || {str(r.remind_date):<30} || {"Yes" if r.sent else "No"}\n' )
        return s