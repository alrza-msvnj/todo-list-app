from typing import Sequence

from core.domain.entities.task import Task
from core.domain.i_repositories.i_task_repository import ITaskRepository
from core.application.dtos.response_dto import ResponseDto
from core.application.contracts.task_contract import TaskContract
from core.application.dtos.task_dtos import TaskDtos


class TaskUseCase(TaskContract):
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def add_task(self, add_task_dto: TaskDtos.AddTaskDto) -> ResponseDto[Task]:
        task: Task | None = self.task_repository.get_task_by_title(add_task_dto.title)
        if task is not None:
            return ResponseDto[Task](None, False, 'A task with the same title already exists.')

        task = Task(add_task_dto.title, add_task_dto.due_date)
        task = self.task_repository.create_task(task)

        return ResponseDto[Task](task)

    def get_task(self, task_id: int) -> ResponseDto[Task]:
        task: Task | None = self.task_repository.get_task(task_id)
        if task is None:
            return ResponseDto[Task](None, False, 'Task does not exist.')

        return ResponseDto[Task](task)

    def get_tasks(self) -> ResponseDto[Sequence[Task]]:
        tasks: Sequence[Task] = self.task_repository.get_tasks()

        return ResponseDto[Sequence[Task]](tasks)

    def edit_task(self, edit_task_dto: TaskDtos.EditTaskDto) -> ResponseDto[Task]:
        task: Task | None = self.task_repository.get_task(edit_task_dto.id)
        if task is None:
            return ResponseDto[Task](None, False, 'Task does not exist.')

        if edit_task_dto.title is not None:
            existing_task: Task | None = self.task_repository.get_task_by_title(edit_task_dto.title)
            if existing_task is not None:
                return ResponseDto[Task](None, False, 'A task with the same title already exists.')

            task.title = edit_task_dto.title

        if edit_task_dto.due_date is not None:
            task.due_date = edit_task_dto.due_date

        return ResponseDto[Task](task)
    
    def remove_task(self, task_id: int) -> ResponseDto[Task]:
        task: Task | None = self.task_repository.get_task(task_id)
        if task is None:
            return ResponseDto[Task](None, False, 'Task does not exist.')

        self.task_repository.delete_task(task)

        return ResponseDto[Task](task)
