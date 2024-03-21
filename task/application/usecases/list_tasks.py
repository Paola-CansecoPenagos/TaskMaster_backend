class ListTasks:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, user_id):
        return self.task_repository.find_by_user_id(user_id)
