from flask import Blueprint, request, jsonify
from task.application.usecases.edit_task import EditTask
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository

edit_task_blueprint = Blueprint('edit_task', __name__)

def initialize_endpoints(repository):
    edit_task_usecase = EditTask(task_repository=repository)

    @edit_task_blueprint.route('/edit', methods=['PUT'])
    def edit_task():
        data = request.get_json()
        user_id = data.get('user_id')
        task_id = data.get('task_id')
        task_data = {key: value for key, value in data.items() if key not in ['user_id', 'task_id'] and value is not None}

        try:
            task = edit_task_usecase.execute(user_id, task_id, task_data)
            return jsonify(task), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500