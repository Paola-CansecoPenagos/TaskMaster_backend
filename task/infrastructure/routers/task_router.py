from flask import Blueprint
from task.infrastructure.controllers.create_task_controller import create_task_blueprint, initialize_endpoints
from task.infrastructure.repositories.task_repository import MongoDBTaskRepository 
from task.infrastructure.controllers.list_tasks_controller import list_tasks_blueprint, initialize_endpoints as list_tasks_endpoints
from task.infrastructure.controllers.list_task_controller import list_task_blueprint, initialize_endpoints as list_task_endpoints

task_router = Blueprint('task_router', __name__)

def initialize_endpoints_create_task(repository):
    initialize_endpoints(repository)
    
def initialize_endpoints_list_tasks(repository):
    list_tasks_endpoints(repository)

def initialize_endpoints_list_task(repository):
    list_task_endpoints(repository)

initialize_endpoints_create_task(MongoDBTaskRepository(connection_string='mongodb://localhost:27017/', database_name='taskMaster'))
initialize_endpoints_list_tasks(MongoDBTaskRepository(connection_string='mongodb://localhost:27017/', database_name='taskMaster'))
initialize_endpoints_list_task(MongoDBTaskRepository(connection_string='mongodb://localhost:27017/', database_name='taskMaster'))

task_router.register_blueprint(create_task_blueprint, url_prefix='/api/tasks')
task_router.register_blueprint(list_tasks_blueprint, url_prefix='/api/tasks')
task_router.register_blueprint(list_task_blueprint, url_prefix='/api/task')