class ListTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, user_id, task_id):
        return self.task_repository.find_by_user_and_task_id(user_id, task_id)
