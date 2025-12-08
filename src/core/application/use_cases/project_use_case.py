from typing import Sequence

from src.core.application.factories.project_factory import ProjectFactory
from src.core.domain.entities.project import Project
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.i_use_cases.i_project_use_case import IProjectUseCase
from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.domain.i_repositories.i_task_repository import ITaskRepository


class ProjectUseCase(IProjectUseCase):
    def __init__(self, project_repository: IProjectRepository, task_repository: ITaskRepository):
        self.project_repository = project_repository
        self.task_repository = task_repository

    def add_project(self, add_project_dto: ProjectDtos.AddProjectDto) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        if len(add_project_dto.name) > 30:
            return ResponseDto[ProjectDtos.ProjectResponseDto](
                success=False,
                message='Name length cannot be more than 30 letters.'
            )

        if add_project_dto.description is not None:
            if len(add_project_dto.description) > 150:
                return ResponseDto[ProjectDtos.ProjectResponseDto](
                    success=False, 
                    message='Description length cannot be more than 150 letters.'
                )

        project: Project | None = self.project_repository.get_project_by_name(add_project_dto.name)
        if project is not None:
            return ResponseDto[ProjectDtos.ProjectResponseDto](
                success=False, 
                message='A project with the same name already exists.'
            )

        project = Project(
            name=add_project_dto.name, 
            description=add_project_dto.description
        )
        project = self.project_repository.create_project(project)

        return ResponseDto[ProjectDtos.ProjectResponseDto](
            result=ProjectFactory.map_to_project_response_dto(project)
        )

    def get_project(self, project_id: int) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        project: Project | None = self.project_repository.get_project(project_id)
        if project is None:
            return ResponseDto[ProjectDtos.ProjectResponseDto](
                success=False, 
                message='Project does not exist.'
            )

        return ResponseDto[ProjectDtos.ProjectResponseDto](
            result=ProjectFactory.map_to_project_response_dto(project)
        )

    def get_projects(self) -> ResponseDto[Sequence[ProjectDtos.ProjectResponseDto]]:
        projects: Sequence[Project] = self.project_repository.get_projects()

        project_response_dtos: Sequence[ProjectDtos.ProjectResponseDto] = []
        for project in projects:
            project_response_dto: ProjectDtos.ProjectResponseDto = ProjectFactory.map_to_project_response_dto(project)
            project_response_dtos.append(project_response_dto)

        return ResponseDto[Sequence[ProjectDtos.ProjectResponseDto]](
            result=project_response_dtos
        )

    def edit_project(self, edit_project_dto: ProjectDtos.EditProjectDto) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        if edit_project_dto.new_name is None and edit_project_dto.new_description is None:
            return ResponseDto[ProjectDtos.ProjectResponseDto](
                success=False, 
                message='Enter a value to edit.'
            )

        project: Project | None = self.project_repository.get_project_by_name(edit_project_dto.name)
        if project is None:
            return ResponseDto[ProjectDtos.ProjectResponseDto](
                success=False, 
                message='Project does not exist.'
            )

        if edit_project_dto.new_name is not None:
            if len(edit_project_dto.new_name) > 30:
                return ResponseDto[ProjectDtos.ProjectResponseDto](
                    success=False, 
                    message='New name length cannot be more than 30 letters.'
                )

            existing_project: Project | None = self.project_repository.get_project_by_name(edit_project_dto.new_name)
            if existing_project is not None:
                return ResponseDto[ProjectDtos.ProjectResponseDto](
                    success=False, 
                    message='A project with the same name already exists.'
                )

            project.name = edit_project_dto.new_name

        if edit_project_dto.new_description is not None:
            if len(edit_project_dto.new_description) > 150:
                return ResponseDto[ProjectDtos.ProjectResponseDto](
                    success=False, 
                    message='New description length cannot be more than 150 letters.'
                )
            
            project.description = edit_project_dto.new_description

        self.project_repository.commit()

        return ResponseDto[ProjectDtos.ProjectResponseDto](
            result=ProjectFactory.map_to_project_response_dto(project)
        )
    
    def remove_project(self, name: str) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        project: Project | None = self.project_repository.get_project_by_name(name)
        if project is None:
            return ResponseDto[ProjectDtos.ProjectResponseDto](
                success=False, 
                message='Project does not exist.'
            )

        project_tasks = self.task_repository.get_tasks(project.id)

        for task in project_tasks:
            self.task_repository.delete_task(task)

        self.project_repository.delete_project(project)

        return ResponseDto[ProjectDtos.ProjectResponseDto](
            result=ProjectFactory.map_to_project_response_dto(project)
        )
