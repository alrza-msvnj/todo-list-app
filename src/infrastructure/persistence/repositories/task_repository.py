from collections.abc import Sequence
from datetime import datetime, timezone

from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from src.core.domain.entities.task import Task
from src.core.domain.i_repositories.i_task_repository import ITaskRepository
from src.infrastructure.persistence.data.session import SessionLocal


class TaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task

    def get_task(self, task_id: int) -> Task | None:
        query = select(Task).where(Task.id == task_id)
        result = self.db.execute(query).scalars().first()

        return result

    def get_task_by_title(self, project_id: int, title: str) -> Task | None:
        query = select(Task).where(Task.project_id == project_id, Task.title == title)
        result = self.db.execute(query).scalars().first()

        return result

    def get_tasks(self, project_id: int | None = None) -> Sequence[Task]:
        query = select(Task)

        if project_id is not None:
            query = query.where(Task.project_id == project_id)

        results = self.db.execute(query).scalars().all()

        return results
    
    def get_overdue_tasks(self) -> Sequence[Task]:
        query = (
            select(Task)
            .where(
                Task.due_date.isnot(None),
                Task.due_date < datetime.now(timezone.utc),
                Task.status.isnot('done')
            )
        )

        result = self.db.scalars(query).all()

        return result

    def delete_task(self, task: Task) -> Task:
        self.db.delete(task)
        self.db.commit()
        
        return task
    
    def commit(self) -> None:
        self.db.commit()
        
        return
