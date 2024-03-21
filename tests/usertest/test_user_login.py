from unittest.mock import MagicMock
import pytest
from user.application.usecases.login_user import LoginUser
from user.domain.entities.user import User
from user.infrastructure.repositories.user_repository import MongoDBUserRepository

@pytest.fixture
def mock_user_repository():
    return MagicMock(spec=MongoDBUserRepository)

def test_login_user_valid_credentials(mock_user_repository):
    user = User("Pio", "paola18@gmail.com", "password123")
    mock_user_repository.find_by_email.return_value = user

    login_user_usecase = LoginUser(user_repository=mock_user_repository)
    logged_user = login_user_usecase.execute("paola18@gmail.com", "password123")

    assert logged_user == user

def test_login_user_invalid_credentials(mock_user_repository):
    mock_user_repository.find_by_email.return_value = None

    login_user_usecase = LoginUser(user_repository=mock_user_repository)
    logged_user = login_user_usecase.execute("pio@gmail.com", "passwrd123")

    assert logged_user is None
