from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.dtos.project_dtos import ProjectDtos


class IProjectUseCase(ABC):
    @abstractmethod
    def add_project(self, add_project_dto: ProjectDtos.AddProjectDto) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        pass

    @abstractmethod
    def get_project(self, project_id: int) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        pass

    @abstractmethod
    def get_projects(self) -> ResponseDto[Sequence[ProjectDtos.ProjectResponseDto]]:
        pass

    @abstractmethod
    def edit_project(self, edit_project_dto: ProjectDtos.EditProjectDto) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        pass
    
    @abstractmethod
    def remove_project(self, name: str) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
        pass
