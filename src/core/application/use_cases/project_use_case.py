from typing import Sequence

from src.core.domain.entities.project import Project
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.contracts.project_contract import ProjectContract
from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.domain.i_repositories.i_task_repository import ITaskRepository


class ProjectUseCase(ProjectContract):
    def __init__(self, project_repository: IProjectRepository, task_repository: ITaskRepository):
        self.project_repository = project_repository
        self.task_repository = task_repository

    def add_project(self, add_project_dto: ProjectDtos.AddProjectDto) -> ResponseDto[Project]:
        if len(add_project_dto.name) > 30:
            return ResponseDto[Project](None, False, 'Name length cannot be more than 30 letters.')

        if add_project_dto.description is not None:
            if len(add_project_dto.description) > 150:
                return ResponseDto[Project](None, False, 'Description length cannot be more than 150 letters.')

        project: Project | None = self.project_repository.get_project_by_name(add_project_dto.name)
        if project is not None:
            return ResponseDto[Project](None, False, 'A project with the same name already exists.')

        project = Project(add_project_dto.name, add_project_dto.description)
        project = self.project_repository.create_project(project)

        return ResponseDto[Project](project)

    def get_project(self, project_id: int) -> ResponseDto[Project]:
        project: Project | None = self.project_repository.get_project(project_id)
        if project is None:
            return ResponseDto[Project](None, False, 'Project does not exist.')

        return ResponseDto[Project](project)

    def get_projects(self) -> ResponseDto[Sequence[Project]]:
        projects: Sequence[Project] = self.project_repository.get_projects()

        return ResponseDto[Sequence[Project]](projects)

    def edit_project(self, edit_project_dto: ProjectDtos.EditProjectDto) -> ResponseDto[Project]:
        if edit_project_dto.new_name is None and edit_project_dto.new_description is None:
            return ResponseDto[Project](None, False, 'Enter a value to edit.')

        project: Project | None = self.project_repository.get_project_by_name(edit_project_dto.name)
        if project is None:
            return ResponseDto[Project](None, False, 'Project does not exist.')

        if edit_project_dto.new_name is not None:
            if len(edit_project_dto.new_name) > 30:
                return ResponseDto[Project](None, False, 'New name length cannot be more than 30 letters.')

            existing_project: Project | None = self.project_repository.get_project_by_name(edit_project_dto.name)
            if existing_project is not None:
                return ResponseDto[Project](None, False, 'A project with the same name already exists.')

            project.name = edit_project_dto.name

        if edit_project_dto.new_description is not None:
            if len(edit_project_dto.new_description) > 150:
                return ResponseDto[Project](None, False, 'New description length cannot be more than 150 letters.')
            
            project.description = edit_project_dto.new_description

        return ResponseDto[Project](project)
    
    def remove_project(self, name: str) -> ResponseDto[Project]:
        project: Project | None = self.project_repository.get_project_by_name(name)
        if project is None:
            return ResponseDto[Project](None, False, 'Project does not exist.')

        project_tasks = self.task_repository.get_tasks(project.id)

        for task in project_tasks:
            self.task_repository.delete_task(task)

        self.project_repository.delete_project(project)

        return ResponseDto[Project](project)
