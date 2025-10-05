from abc import ABC, abstractmethod
from collections.abc import Sequence

from domain.entities.project import Project
from application.dtos.project_dtos import ProjectDtos


class ProjectContract(ABC):
    @abstractmethod
    def add_project(self, add_project_dto: ProjectDtos.AddProjectDto) -> Project:
        pass

    @abstractmethod
    def get_project(self, project_id: int) -> Project:
        pass

    @abstractmethod
    def get_projects(self) -> Sequence[Project]:
        pass

    @abstractmethod
    def edit_project(self, edit_project_dto: ProjectDtos.EditProjectDto) -> Project:
        pass
    
    @abstractmethod
    def remove_project(self, project_id: int) -> Project:
        pass
