from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.core.domain.entities.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    def create_task(self, task: Task) -> Task:
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> Task | None:
        pass

    @abstractmethod
    def get_task_by_title(self, title: str) -> Task | None:
        pass

    @abstractmethod
    def get_tasks(self) -> Sequence[Task]:
        pass

    @abstractmethod
    def delete_task(self, task: Task) -> Task:
        pass
