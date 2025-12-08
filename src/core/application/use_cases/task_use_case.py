from datetime import datetime, timezone
from typing import Sequence

from src.core.application.factories.task_factory import TaskFactory
from src.core.domain.entities.project import Project
from src.core.domain.entities.task import Task
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.core.domain.i_repositories.i_task_repository import ITaskRepository
from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.i_use_cases.i_task_use_case import ITaskUseCase
from src.core.application.dtos.task_dtos import TaskDtos


class TaskUseCase(ITaskUseCase):
    def __init__(self, task_repository: ITaskRepository, project_repository: IProjectRepository):
        self.task_repository = task_repository
        self.project_repository = project_repository

    def add_task(self, add_task_dto: TaskDtos.AddTaskDto) -> ResponseDto[TaskDtos.TaskResponseDto]:
        if len(add_task_dto.title) > 30:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'Title length cannot be more than 30 letters.')
        
        if add_task_dto.description is not None:
            if len(add_task_dto.description) > 150:
                return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'Description length cannot be more than 150 letters.')

        if add_task_dto.due_date is not None:
            try:
                datetime.strptime(add_task_dto.due_date, '%Y-%m-%d')
                return True
            except ValueError:
                return False

        project: Project | None = self.project_repository.get_project_by_name(add_task_dto.project_name)
        if project is None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, f'No project found with the name {add_task_dto.project_name}.')

        task: Task | None = self.task_repository.get_task_by_title(project.id, add_task_dto.title)
        if task is not None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'A task with the same title already exists.')

        task = Task(
            project_id=project.id, 
            title=add_task_dto.title, 
            description=add_task_dto.description, 
            due_date=add_task_dto.due_date
        )
        task = self.task_repository.create_task(task)

        return ResponseDto[TaskDtos.TaskResponseDto](TaskFactory.map_to_task_response_dto(task))

    def get_task(self, task_id: int) -> ResponseDto[TaskDtos.TaskResponseDto]:
        task: Task | None = self.task_repository.get_task(task_id)
        if task is None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'Task does not exist.')

        return ResponseDto[TaskDtos.TaskResponseDto](TaskFactory.map_to_task_response_dto(task))

    def get_tasks(self, project_name: str | None = None) -> ResponseDto[Sequence[TaskDtos.TaskResponseDto]]:
        project_id: int | None = None
        if project_name is not None:
            project: Project | None = self.project_repository.get_project_by_name(project_name)
            if project is None:
                return ResponseDto[Sequence[TaskDtos.TaskResponseDto]](None, False, f'No project found with the name {project_name}.')
            
            project_id = project.id

        tasks: Sequence[TaskDtos.TaskResponseDto] = self.task_repository.get_tasks(project_id)

        task_response_dtos: Sequence[TaskDtos.TaskResponseDto] = []
        for task in tasks:
            task_response_dto: TaskDtos.TaskResponseDto = TaskFactory.map_to_task_response_dto(task)
            task_response_dtos.append(task_response_dto)

        return ResponseDto[Sequence[TaskDtos.TaskResponseDto]](task_response_dtos)

    def edit_task(self, edit_task_dto: TaskDtos.EditTaskDto) -> ResponseDto[TaskDtos.TaskResponseDto]:
        if edit_task_dto.new_title is None and edit_task_dto.new_description is None and edit_task_dto.new_due_date is None and edit_task_dto.new_status is None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'Enter a value to edit.')

        project: Project | None = self.project_repository.get_project_by_name(edit_task_dto.project_name)
        if project is None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, f'No project found with the name {edit_task_dto.project_name}.')

        task: Task | None = self.task_repository.get_task_by_title(project.id, edit_task_dto.title)
        if task is None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'Task does not exist.')

        if edit_task_dto.new_title is not None:
            if len(edit_task_dto.new_title) > 30:
                return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'New title length cannot be more than 30 letters.')

            existing_task: Task | None = self.task_repository.get_task_by_title(project.id, edit_task_dto.new_title)
            if existing_task is not None:
                return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'A task with the same title already exists.')

            task.title = edit_task_dto.new_title

        if edit_task_dto.new_description is not None:
            if len(edit_task_dto.new_description) > 150:
                return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'New description length cannot be more than 150 letters.')

            task.description = edit_task_dto.new_description

        if edit_task_dto.new_due_date is not None:
            task.due_date = edit_task_dto.new_due_date

        if edit_task_dto.new_status is not None:
            if edit_task_dto.new_status != 'todo' and edit_task_dto.new_status != 'doing' and edit_task_dto.new_status != 'done':
                return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'New status should be one of these values: todo, doing, done.')

            task.status = edit_task_dto.new_status

        return ResponseDto[TaskDtos.TaskResponseDto](TaskFactory.map_to_task_response_dto(task))
    
    def remove_task(self, project_name: str, title: str) -> ResponseDto[TaskDtos.TaskResponseDto]:
        project: Project | None = self.project_repository.get_project_by_name(project_name)
        if project is None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, f'No project found with the name {project_name}.')

        task: Task | None = self.task_repository.get_task_by_title(project.id, title)
        if task is None:
            return ResponseDto[TaskDtos.TaskResponseDto](None, False, 'Task does not exist.')

        self.task_repository.delete_task(task)

        return ResponseDto[TaskDtos.TaskResponseDto](TaskFactory.map_to_task_response_dto(task))
