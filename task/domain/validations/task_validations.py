import re

def validate_task(task):
    if not isinstance(task):
        raise ValueError("Invalid task object")
    if not task.title:
        raise ValueError("Title cannot be empty")
