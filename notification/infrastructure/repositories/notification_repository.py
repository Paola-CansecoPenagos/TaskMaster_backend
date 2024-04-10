from bson import ObjectId
from pymongo import MongoClient
from notification.domain.entities.notification import Notification

class MongoDBNotificationRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.user_collection = self.db['users']

    def save(self, notification: Notification):
        notification_data = notification.__dict__.copy()
        notification_data.pop('user_id', None)
        self.user_collection.update_one(
            {'_id': ObjectId(notification.user_id)},
            {'$push': {'notifications': notification_data}}
        )

    def find_by_user_id(self, user_id):
        user = self.user_collection.find_one({'_id': ObjectId(user_id)}, {'notifications': 1})
        return user.get('notifications', [])
