import pytest
from unittest.mock import MagicMock
from task.application.usecases.list_task import ListTask
from task.domain.entities.task import Task
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository

@pytest.fixture
def task_repository():
    return MagicMock(spec=MongoDBTaskRepository)

def test_list_task(task_repository):
    task_repository.find_by_user_and_task_id.return_value = {
        "title": "Creacion de endpoints4",
        "start_time": "12:00",
        "end_time": "12:00",
        "label": "Móviles",
        "description": "Crear los endpoints para listar las tareas",
        "type": "Escolar",
        "deadline": "19 de marzo de 2024",
        "subtasks": [
            {
                "details": "Se debe de crear una API con arquitectura hexagonal"
            },
            {
                "details": "Agregar el endpoint para poder ver las tareas que tiene el usuario "
            }
        ],
        "reminders": [
            {
                "reminder_time": "12:00 am"
            },
            {
                "reminder_time": "12:30 am"
            }
        ],
    }
    
    list_task_usecase = ListTask(task_repository=task_repository)
    task = list_task_usecase.execute(user_id="user_id", task_id="task_id")
    assert task is not None
    assert task["title"] == "Test Task"