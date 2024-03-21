# project/task/tests/test_task.py
import pytest
from unittest.mock import MagicMock
from task.application.usecases.create_task import CreateTask
from task.domain.entities.task import Task
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository

@pytest.fixture
def task_repository():
    return MagicMock(spec=MongoDBTaskRepository)

def test_create_task(task_repository):
    create_task_usecase = CreateTask(task_repository=task_repository)
    task = Task(
        title="Test Task",
        start_time="08:00",
        end_time="10:00:00",
        label="Escolar",
        description="Ejecutar pruebas automaticas",
        type="Test",
        deadline="21 de marzo de 2024",
        subtasks=[
            {
                "details": "Definir cuales seran las pruebas automatizadas"
            },
            {
                "details": "Comprobar que las pruebas sean exitosas"
            }
        ],
        reminders=[]
    )
    create_task_usecase.execute(task, user_id="user_id")
    task_repository.save.assert_called_once_with(task, user_id="user_id")