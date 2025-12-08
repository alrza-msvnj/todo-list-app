from collections.abc import Sequence

from src.core.domain.entities.task import Task
from src.core.domain.i_repositories.i_task_repository import ITaskRepository
from src.infrastructure.data.in_memory_database import InMemoryDatabase


class TaskRepository(ITaskRepository):
    def __init__(self, in_memory_database: InMemoryDatabase):
        self.db = in_memory_database

    def create_task(self, task: Task) -> Task:
        return self.db.create_task(task)

    def get_task(self, task_id: int) -> Task | None:
        for task in self.db.tasks:
            if task.id == task_id:
                return task
        
        return None
    
    def get_task_by_title(self, project_id: int, title: str) -> Task | None:
        for task in self.db.tasks:
            if task.project_id == project_id and task.title == title:
                return task
        
        return None

    def get_tasks(self, project_id: int | None = None) -> Sequence[Task]:
        tasks: Sequence[Task] = self.db.tasks

        if project_id is not None:
            for task in tasks:
                if task.project_id != project_id:
                    tasks.remove(task)

        return tasks

    def delete_task(self, task: Task) -> Task:
        self.db.tasks.remove(task)

        return task
