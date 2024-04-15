from flask import Blueprint, request, jsonify
from task.application.usecases.delete_task import DeleteTask
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository

delete_task_blueprint = Blueprint('delete_task', __name__)

def initialize_endpoints(repository):
    delete_task_usecase = DeleteTask(task_repository=repository)

    @delete_task_blueprint.route('/delete/<user_id>/<task_id>', methods=['DELETE'])
    def delete_task(user_id, task_id):
        try:
            delete_task_usecase.execute(user_id, task_id)
            return jsonify({"message": "Task deleted successfully"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500