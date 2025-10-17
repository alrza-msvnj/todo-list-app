from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.core.domain.entities.task import Task
from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.dtos.task_dtos import TaskDtos


class TaskContract(ABC):
    @abstractmethod
    def add_task(self, add_task_dto: TaskDtos.AddTaskDto) -> ResponseDto[Task]:
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> ResponseDto[Task]:
        pass

    @abstractmethod
    def get_tasks(self, project_name: str | None = None) -> ResponseDto[Sequence[Task]]:
        pass

    @abstractmethod
    def edit_task(self, edit_task_dto: TaskDtos.EditTaskDto) -> ResponseDto[Task]:
        pass
    
    @abstractmethod
    def remove_task(self, project_name: str, title: str) -> ResponseDto[Task]:
        pass
