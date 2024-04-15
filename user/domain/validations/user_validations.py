import re

def validate_email(email):
    email_regex = r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[\w]+$'
    if not re.match(email_regex, email):
        return False
    return True

def validate_name(name):
    return name.isalpha() and not any(char.isdigit() for char in name)