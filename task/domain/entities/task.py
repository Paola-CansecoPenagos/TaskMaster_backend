class Task:
    def __init__(self, title, start_time, end_time, label, description, type, deadline, subtasks=None, reminders=None):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.label = label
        self.description = description
        self.type = type
        self.deadline = deadline
        self.subtasks = subtasks if subtasks else []
        self.reminders = reminders if reminders else []
