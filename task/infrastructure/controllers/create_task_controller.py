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
        title = data.get('title', '').strip()
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        label = data.get('label', '').strip()
        description = data.get('description', '').strip()
        type = data.get('type', '').strip()
        deadline = data.get('deadline')
        subtasks = data.get('subtasks', [])
        reminders = data.get('reminders', [])

        # Validación de campos obligatorios
        required_fields = [title]
        if not all(required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Validación de longitud de campos
        if any(len(field) > 500 or len(field) < 1 for field in [title, label, description, type] if field):
            return jsonify({"error": "Field length out of allowed range"}), 400

        # Creación y guardado de la tarea
        try:
            task = Task(title, start_time, end_time, label, description, type, deadline, subtasks, reminders)
            create_task_usecase.execute(task, user_id)
            return jsonify({"message": "Task created successfully"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
