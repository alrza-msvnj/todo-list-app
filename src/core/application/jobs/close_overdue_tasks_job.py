from collections.abc import Sequence
from datetime import datetime, timezone
from src.core.domain.entities.task import Task
from src.core.domain.i_repositories.i_task_repository import ITaskRepository


class CloseOverdueTasksJob:
   def __init__(self, task_repository: ITaskRepository):
      self.task_repository = task_repository

   def execute(self) -> None:
      tasks: Sequence[Task] = self.task_repository.get_overdue_tasks()

      now = datetime.now(timezone.utc)
      for task in tasks:
         task.status = 'done'
         task.closed_at = now
      
      self.task_repository.commit()
