from typing import Sequence

from src.core.domain.entities.project import Project
from src.core.domain.entities.task import Task
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.core.domain.i_repositories.i_task_repository import ITaskRepository
from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.contracts.task_contract import TaskContract
from src.core.application.dtos.task_dtos import TaskDtos


class TaskUseCase(TaskContract):
    def __init__(self, task_repository: ITaskRepository, project_repository: IProjectRepository):
        self.task_repository = task_repository
        self.project_repository = project_repository

    def add_task(self, add_task_dto: TaskDtos.AddTaskDto) -> ResponseDto[Task]:
        project: Project | None = self.project_repository.get_project_by_name(add_task_dto.project_name)
        if project is None:
            return ResponseDto[Task](None, False, f'No project found with the name {add_task_dto.project_name}.')

        task: Task | None = self.task_repository.get_task_by_title(project.id, add_task_dto.title)
        if task is not None:
            return ResponseDto[Task](None, False, 'A task with the same title already exists.')

        task = Task(project.id, add_task_dto.title, add_task_dto.due_date)
        task = self.task_repository.create_task(task)

        return ResponseDto[Task](task)

    def get_task(self, task_id: int) -> ResponseDto[Task]:
        task: Task | None = self.task_repository.get_task(task_id)
        if task is None:
            return ResponseDto[Task](None, False, 'Task does not exist.')

        return ResponseDto[Task](task)

    def get_tasks(self, project_name: str | None = None) -> ResponseDto[Sequence[Task]]:
        project_id: int | None = None
        if project_name is not None:
            project: Project | None = self.project_repository.get_project_by_name(project_name)
            if project is None:
                return ResponseDto[Sequence[Task]](None, False, f'No project found with the name {project_name}.')
            
            project_id = project.id

        tasks: Sequence[Task] = self.task_repository.get_tasks(project_id)

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
    
    def remove_task(self, project_name: str, title: str) -> ResponseDto[Task]:
        project: Project | None = self.project_repository.get_project_by_name(project_name)
        if project is None:
            return ResponseDto[Task](None, False, f'No project found with the name {project_name}.')

        task: Task | None = self.task_repository.get_task_by_title(project.id, title)
        if task is None:
            return ResponseDto[Task](None, False, 'Task does not exist.')

        self.task_repository.delete_task(task)

        return ResponseDto[Task](task)
