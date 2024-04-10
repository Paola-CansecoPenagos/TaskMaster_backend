from flask import Blueprint
from notification.infrastructure.controllers.create_notification_controller import create_notification_blueprint, initialize_create_notification_endpoint
from notification.infrastructure.controllers.list_notification_controller import list_notifications_blueprint, initialize_list_notifications_endpoint
from notification.infrastructure.repositories.notification_repository import MongoDBNotificationRepository

notification_router = Blueprint('notification_router', __name__)

def initialize_notification_endpoints(repository):
    initialize_create_notification_endpoint(repository)
    initialize_list_notifications_endpoint(repository)

repository = MongoDBNotificationRepository(connection_string='mongodb://localhost:27017/', database_name='taskMaster')
initialize_notification_endpoints(repository)

notification_router.register_blueprint(create_notification_blueprint, url_prefix='/api/notifications')
notification_router.register_blueprint(list_notifications_blueprint, url_prefix='/api/notifications')
