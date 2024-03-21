from flask import Blueprint, request, jsonify
from task.application.usecases.list_task import ListTask
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository

list_task_blueprint = Blueprint('list_task', __name__)

def initialize_endpoints(repository):
    list_task_usecase = ListTask(task_repository=repository)

    @list_task_blueprint.route('/list', methods=['GET'])
    def list_task():
        user_id = request.args.get('user_id')
        task_id = request.args.get('task_id')
        task = list_task_usecase.execute(user_id, task_id)
        if task:
            task['id'] = task_id
            return jsonify(task), 200
        else:
            return jsonify({"message": "Task not found"}), 404
