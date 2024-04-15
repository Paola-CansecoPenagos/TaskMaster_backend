class EditTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, user_id, task_id, updated_task_data):
        task = self.task_repository.find_by_user_and_task_id(user_id, task_id)
        if not task:
            raise ValueError("Task not found")

        updated_fields = {}
        for key, value in updated_task_data.items():
            if value is not None and value != "":
                if 1 <= len(str(value)) <= 500:  # Validar longitud si es necesario
                    updated_fields[f'tasks.$.{key}'] = value
                else:
                    raise ValueError(f"Invalid value for {key}")

        if not updated_fields:
            raise ValueError("No valid fields provided for update")

        self.task_repository.update_task(user_id, task_id, updated_fields)
        return self.task_repository.find_by_user_and_task_id(user_id, task_id)
