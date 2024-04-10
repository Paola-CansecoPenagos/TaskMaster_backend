from notification.domain.entities.notification import Notification
from notification.domain.validations.notification_validations import validate_notification

class CreateNotification:
    def __init__(self, notification_repository):
        self.notification_repository = notification_repository

    def execute(self, user_id, message, type):
        notification = Notification(user_id, message, type)
        validate_notification(notification)
        self.notification_repository.save(notification)
