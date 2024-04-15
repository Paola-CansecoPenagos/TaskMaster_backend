from bson import ObjectId
from pymongo import MongoClient
from user.infrastructure.repositories.user_repository import MongoDBUserRepository
from task.domain.entities.task import Task

class MongoDBTaskRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.user_repository = MongoDBUserRepository(connection_string, database_name)

    def save(self, task: Task, user_id):
        user_id = ObjectId(user_id)
        user = self.user_repository.collection.find_one({'_id': user_id})
        if user:
            task_id = ObjectId()  
            task.id = str(task_id) 
            user_tasks = user.get('tasks', [])
            user_tasks.append(task.__dict__)
            self.user_repository.collection.update_one({'_id': user_id}, {'$set': {'tasks': user_tasks}})
        else:
            raise ValueError("User not found")

    def find_by_user_id(self, user_id):
        user_id = ObjectId(user_id)
        user = self.user_repository.collection.find_one({'_id': user_id})
        if user:
            return user.get('tasks', [])
        else:
            return None

    def find_by_user_and_task_id(self, user_id, task_id):
        user_id = ObjectId(user_id)
        user = self.user_repository.collection.find_one({'_id': user_id})
        if user:
            tasks = user.get('tasks', [])
            for task in tasks:
                if task.get('id') == task_id:
                    return task
            return None
        else:
            return None
        
    def update_task(self, user_id, task_id, updated_fields):
        user_id = ObjectId(user_id)
        result = self.user_repository.collection.update_one(
            {'_id': user_id, 'tasks.id': task_id},
            {'$set': updated_fields}
        )
        if result.modified_count == 0:
            raise ValueError("Task update failed or no fields updated")
        
    def delete_task(self, user_id, task_id):
        user_id = ObjectId(user_id)
        task_id = ObjectId(task_id) 
        result = self.user_repository.collection.update_one(
            {'_id': user_id},
            {'$pull': {'tasks': {'id': str(task_id)}}}
        )
        if result.modified_count == 0:
            raise ValueError("Task deletion failed or task not found")