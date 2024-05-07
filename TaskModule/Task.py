import datetime as dt
class Task:
    def __init__(self, name: str, date: dt.date, description: str ) -> None:
        self.name = name
        self.due_date = date
        self.description = description
        self.done = False
