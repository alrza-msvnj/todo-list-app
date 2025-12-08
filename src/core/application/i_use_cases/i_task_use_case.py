from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.dtos.task_dtos import TaskDtos


class ITaskUseCase(ABC):
    @abstractmethod
    def add_task(self, add_task_dto: TaskDtos.AddTaskDto) -> ResponseDto[TaskDtos.TaskResponseDto]:
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> ResponseDto[TaskDtos.TaskResponseDto]:
        pass

    @abstractmethod
    def get_tasks(self, project_name: str | None = None) -> ResponseDto[Sequence[TaskDtos.TaskResponseDto]]:
        pass

    @abstractmethod
    def edit_task(self, edit_task_dto: TaskDtos.EditTaskDto) -> ResponseDto[TaskDtos.TaskResponseDto]:
        pass
    
    @abstractmethod
    def remove_task(self, project_name: str, title: str) -> ResponseDto[TaskDtos.TaskResponseDto]:
        pass
