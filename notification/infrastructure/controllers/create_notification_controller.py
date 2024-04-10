from flask import Blueprint, request, jsonify
from notification.application.usecases.create_notification import CreateNotification
from notification.infrastructure.repositories.notification_repository import MongoDBNotificationRepository

create_notification_blueprint = Blueprint('create_notification', __name__)

def initialize_create_notification_endpoint(repository):
    create_notification_usecase = CreateNotification(notification_repository=repository)

    @create_notification_blueprint.route('/create', methods=['POST'])
    def create_notification():
        data = request.get_json()
        user_id = data['user_id']
        message = data['message']
        type = data['type']
        try:
            create_notification_usecase.execute(user_id, message, type)
            return jsonify({"message": "Notification created successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
