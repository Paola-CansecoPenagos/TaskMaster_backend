import pytest
from unittest.mock import MagicMock
from task.application.usecases.list_tasks import ListTasks
from task.domain.entities.task import Task
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository

@pytest.fixture
def task_repository():
    return MagicMock(spec=MongoDBTaskRepository)

def test_list_tasks(task_repository):
    task_repository.find_by_user_id.return_value = [
        {
            "end_time": "12:00",
            "id": null,
            "start_time": "12:00",
            "title": "Creacion de endpoints"
        },
        {
            "end_time": "12:00",
            "id": null,
            "start_time": "12:00",
            "title": "Creacion de endpoints2"
        },
        {
            "end_time": "12:00",
            "id": "65f91272404d57a66ab6d1da",
            "start_time": "12:00",
            "title": "Creacion de endpoints3"
        },
        {
            "end_time": "12:00",
            "id": "65f91c99583a4123697f2f5f",
            "start_time": "12:00",
            "title": "Creacion de endpoints4"
        }
    ]
    list_tasks_usecase = ListTasks(task_repository=task_repository)
    tasks = list_tasks_usecase.execute(user_id="user_id")
    assert tasks is not None
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"
