class Notification:
    def __init__(self, user_id, message, type, status='unread'):
        from datetime import datetime
        self.user_id = user_id
        self.message = message
        self.type = type
        self.status = status
        self.created_at = datetime.now()
