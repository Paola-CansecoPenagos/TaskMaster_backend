from flask import Blueprint, request, jsonify
from task.application.usecases.list_tasks import ListTasks
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository

list_tasks_blueprint = Blueprint('list_tasks', __name__)

def initialize_endpoints(repository):
    list_tasks_usecase = ListTasks(task_repository=repository)

    @list_tasks_blueprint.route('/list', methods=['GET'])
    def list_tasks():
        user_id = request.args.get('user_id')
        tasks = list_tasks_usecase.execute(user_id)
        if tasks:
            task_list = []
            for task in tasks:
                task_list.append({
                    'id': task.get('id'), 
                    'title': task.get('title'),
                    'start_time': task.get('start_time'),
                    'end_time': task.get('end_time')
                })
            return jsonify(task_list), 200
        else:
            return jsonify({"message": "No tasks found for the user"}), 404