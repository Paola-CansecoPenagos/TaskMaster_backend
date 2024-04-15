class DeleteTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, user_id, task_id):
        task = self.task_repository.find_by_user_and_task_id(user_id, task_id)
        if not task:
            raise ValueError("Task not found")
        self.task_repository.delete_task(user_id, task_id)