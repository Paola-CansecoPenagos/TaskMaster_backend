import pytest
from unittest.mock import MagicMock
from notification.application.usecases.list_notifications import ListNotifications
from notification.infrastructure.repositories.notification_repository import MongoDBNotificationRepository

@pytest.fixture
def notification_repository():
    return MagicMock(spec=MongoDBNotificationRepository)

def test_list_notifications(notification_repository):
    list_notifications_usecase = ListNotifications(notification_repository=notification_repository)
    user_id = "6615fcba838a44ccf23d8bcc"
    list_notifications_usecase.execute(user_id=user_id)
    notification_repository.find_by_user_id.assert_called_once_with(user_id)
