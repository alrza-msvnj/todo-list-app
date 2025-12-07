import datetime
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
        if len(add_task_dto.title) > 30:
            return ResponseDto[Task](None, False, 'Title length cannot be more than 30 letters.')
        
        if add_task_dto.description is not None:
            if len(add_task_dto.description) > 150:
                return ResponseDto[Task](None, False, 'Description length cannot be more than 150 letters.')

        if add_task_dto.due_date is not None:
            try:
                datetime.strptime(add_task_dto.due_date, format='')
                return True
            except ValueError:
                return False

        project: Project | None = self.project_repository.get_project_by_name(add_task_dto.project_name)
        if project is None:
            return ResponseDto[Task](None, False, f'No project found with the name {add_task_dto.project_name}.')

        task: Task | None = self.task_repository.get_task_by_title(project.id, add_task_dto.title)
        if task is not None:
            return ResponseDto[Task](None, False, 'A task with the same title already exists.')

        task = Task(project.id, add_task_dto.title, add_task_dto.description, add_task_dto.due_date)
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
        if edit_task_dto.new_title is None and edit_task_dto.new_description is None and edit_task_dto.new_due_date is None and edit_task_dto.new_status is None:
            return ResponseDto[Task](None, False, 'Enter a value to edit.')

        project: Project | None = self.project_repository.get_project_by_name(edit_task_dto.project_name)
        if project is None:
            return ResponseDto[Task](None, False, f'No project found with the name {edit_task_dto.project_name}.')

        task: Task | None = self.task_repository.get_task_by_title(project.id, edit_task_dto.title)
        if task is None:
            return ResponseDto[Task](None, False, 'Task does not exist.')

        if edit_task_dto.new_title is not None:
            if len(edit_task_dto.new_title) > 30:
                return ResponseDto[Task](None, False, 'New title length cannot be more than 30 letters.')

            existing_task: Task | None = self.task_repository.get_task_by_title(project.id, edit_task_dto.new_title)
            if existing_task is not None:
                return ResponseDto[Task](None, False, 'A task with the same title already exists.')

            task.title = edit_task_dto.new_title

        if edit_task_dto.new_description is not None:
            if len(edit_task_dto.new_description) > 150:
                return ResponseDto[Task](None, False, 'New description length cannot be more than 150 letters.')

            task.description = edit_task_dto.new_description

        if edit_task_dto.new_due_date is not None:
            task.due_date = edit_task_dto.new_due_date

        if edit_task_dto.new_status is not None:
            if edit_task_dto.new_status != 'todo' and edit_task_dto.new_status != 'doing' and edit_task_dto.new_status != 'done':
                return ResponseDto[Task](None, False, 'New status should be one of these values: todo, doing, done.')

            task.status = edit_task_dto.new_status

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
