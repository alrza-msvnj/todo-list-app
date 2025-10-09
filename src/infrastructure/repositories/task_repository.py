from collections.abc import Sequence

from core.domain.entities.task import Task
from core.domain.i_repositories.i_task_repository import ITaskRepository
from infrastructure.data.in_memory_database import InMemoryDatabase


class TaskRepository(ITaskRepository):
    def __init__(self, in_memory_database: InMemoryDatabase):
        self.db = in_memory_database

    def create_task(self, task: Task) -> Task:
        self.db.tasks.append(task)

        return task

    def get_task(self, task_id: int) -> Task | None:
        for task in self.db.tasks:
            if task.id == task_id:
                return task
        
        return None
    
    def get_task_by_title(self, title: str) -> Task | None:
        for task in self.db.tasks:
            if task.title == title:
                return task
        
        return None

    def get_tasks(self) -> Sequence[Task]:
        return self.db.tasks

    def delete_task(self, task: Task) -> Task:
        self.db.tasks.remove(task)

        return task
