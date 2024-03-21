class CreateTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, task, user_id):
        self.task_repository.save(task, user_id)