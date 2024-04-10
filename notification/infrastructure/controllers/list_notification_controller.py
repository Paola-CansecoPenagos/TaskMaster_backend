from flask import Blueprint, request, jsonify
from notification.application.usecases.list_notifications import ListNotifications
from notification.infrastructure.repositories.notification_repository import MongoDBNotificationRepository

list_notifications_blueprint = Blueprint('list_notifications', __name__)

def initialize_list_notifications_endpoint(repository):
    list_notifications_usecase = ListNotifications(notification_repository=repository)

    @list_notifications_blueprint.route('/list', methods=['GET'])
    def list_notifications():
        user_id = request.args.get('user_id')
        try:
            notifications = list_notifications_usecase.execute(user_id)
            return jsonify(notifications), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 404
