def validate_notification(notification):
    if not notification.message:
        raise ValueError("Notification message cannot be empty")
    if notification.type not in ['info', 'alert', 'reminder']:
        raise ValueError("Invalid notification type")
