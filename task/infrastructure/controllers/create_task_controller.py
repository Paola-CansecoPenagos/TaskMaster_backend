from flask import Blueprint, request, jsonify
from task.application.usecases.create_task import CreateTask
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository
from task.domain.entities.task import Task

create_task_blueprint = Blueprint('create_task', __name__)

def initialize_endpoints(repository):
    create_task_usecase = CreateTask(task_repository=repository)

    @create_task_blueprint.route('/create', methods=['POST'])
    def create_task():
        data = request.get_json()
        user_id = data.get('user_id') 
        title = data.get('title')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        label = data.get('label')
        description = data.get('description')
        type = data.get('type')
        deadline = data.get('deadline')
        subtasks = data.get('subtasks', [])
        reminders = data.get('reminders', [])

        task = Task(title, start_time, end_time, label, description, type, deadline, subtasks, reminders)
        create_task_usecase.execute(task, user_id)
        return jsonify({"message": "Task created successfully"}), 201
