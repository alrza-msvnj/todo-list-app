from typing import Sequence

from src.core.domain.entities.project import Project
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.contracts.project_contract import ProjectContract
from src.core.application.dtos.project_dtos import ProjectDtos


class ProjectUseCase(ProjectContract):
    def __init__(self, project_repository: IProjectRepository):
        self.project_repository = project_repository

    def add_project(self, add_project_dto: ProjectDtos.AddProjectDto) -> ResponseDto[Project]:
        project: Project | None = self.project_repository.get_project_by_name(add_project_dto.name)
        if project is not None:
            return ResponseDto[Project](None, False, 'A project with the same name already exists.')

        project = Project(add_project_dto.name)
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
        project: Project | None = self.project_repository.get_project(edit_project_dto.id)
        if project is None:
            return ResponseDto[Project](None, False, 'Project does not exist.')

        existing_project: Project | None = self.project_repository.get_project_by_name(edit_project_dto.name)
        if existing_project is not None:
            return ResponseDto[Project](None, False, 'A project with the same name already exists.')

        project.name = edit_project_dto.name

        return ResponseDto[Project](project)
    
    def remove_project(self, project_id: int) -> ResponseDto[Project]:
        project: Project | None = self.project_repository.get_project(project_id)
        if project is None:
            return ResponseDto[Project](None, False, 'Project does not exist.')

        self.project_repository.delete_project(project)

        return ResponseDto[Project](project)
