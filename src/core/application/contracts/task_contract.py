from abc import ABC, abstractmethod
from collections.abc import Sequence

from domain.entities.task import Task
from application.dtos.task_dtos import TaskDtos


class TaskContract(ABC):
    @abstractmethod
    def add_task(self, add_task_dto: TaskDtos.AddTaskDto) -> Task:
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> Task:
        pass

    @abstractmethod
    def get_tasks(self) -> Sequence[Task]:
        pass

    @abstractmethod
    def edit_task(self, edit_task_dto: TaskDtos.EditTaskDto) -> Task:
        pass
    
    @abstractmethod
    def remove_task(self, task_id: int) -> Task:
        pass
