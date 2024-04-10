class ListNotifications:
    def __init__(self, notification_repository):
        self.notification_repository = notification_repository

    def execute(self, user_id):
        return self.notification_repository.find_by_user_id(user_id)
