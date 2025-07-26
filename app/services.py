from app.models import Task, TaskCreate

class TaskService:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def get_all(self):
        return self.tasks

    def get(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def create(self, task_data: TaskCreate):
        task = Task(id=self.counter, **task_data.dict())
        self.tasks.append(task)
        self.counter += 1
        return task

    def update(self, task_id: int, task_data: TaskCreate):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                updated = Task(id=task_id, **task_data.dict())
                self.tasks[i] = updated
                return updated
        return None

    def delete(self, task_id: int):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                return self.tasks.pop(i)
        return None
