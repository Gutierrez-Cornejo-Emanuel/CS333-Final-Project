class ReminderList:
    def __init__(self) -> None:
        self.reminders = []
    def add_reminder(self, rem):
        self.reminders.append(rem)
    def check_reminders(self):
        s = ""
        for r in self.reminders:
            check = r.checkReminder()
            if r:
                s += check
        return s
