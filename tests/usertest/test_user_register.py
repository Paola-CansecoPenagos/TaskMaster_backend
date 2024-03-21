from unittest.mock import MagicMock
import pytest
from user.application.usecases.register_user import RegisterUser
from user.domain.entities.user import User
from user.infrastructure.repositories.user_repository import MongoDBUserRepository

@pytest.fixture
def mock_user_repository():
    return MagicMock(spec=MongoDBUserRepository)

 
def test_register_user_valid_email(mock_user_repository):
    register_user_usecase = RegisterUser(user_repository=mock_user_repository)
    register_user_usecase.execute("Pio", "paola18@gmail.com", "password123")
    mock_user_repository.save.assert_called_once()

def test_register_user_invalid_email(mock_user_repository):
    register_user_usecase = RegisterUser(user_repository=mock_user_repository)
    with pytest.raises(ValueError):
        register_user_usecase.execute("Pio", "paola18gmail.com", "password123")
