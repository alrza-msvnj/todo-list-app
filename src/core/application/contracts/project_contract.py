from abc import ABC, abstractmethod
from collections.abc import Sequence

from domain.entities.project import Project
from core.application.dtos.response_dto import ResponseDto
from application.dtos.project_dtos import ProjectDtos


class ProjectContract(ABC):
    @abstractmethod
    def add_project(self, add_project_dto: ProjectDtos.AddProjectDto) -> ResponseDto[Project]:
        pass

    @abstractmethod
    def get_project(self, project_id: int) -> ResponseDto[Project]:
        pass

    @abstractmethod
    def get_projects(self) -> ResponseDto[Sequence[Project]]:
        pass

    @abstractmethod
    def edit_project(self, edit_project_dto: ProjectDtos.EditProjectDto) -> ResponseDto[Project]:
        pass
    
    @abstractmethod
    def remove_project(self, project_id: int) -> ResponseDto[Project]:
        pass
