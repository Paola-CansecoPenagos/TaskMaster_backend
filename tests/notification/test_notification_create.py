import pytest
from unittest.mock import MagicMock
from notification.application.usecases.create_notification import CreateNotification
from notification.domain.entities.notification import Notification
from notification.infrastructure.repositories.notification_repository import MongoDBNotificationRepository

@pytest.fixture
def notification_repository():
    return MagicMock(spec=MongoDBNotificationRepository)

def test_create_notification(notification_repository):
    create_notification_usecase = CreateNotification(notification_repository=notification_repository)
    notification = Notification(
        user_id="6615fcba838a44ccf23d8bcc",
        message="Reminder: Meeting at noon",
        type="reminder"
    )
    create_notification_usecase.execute(user_id="user123", message="Reminder: Meeting at noon", type="reminder")
    notification_repository.save.assert_called_once_with(notification)
