from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.core.domain.entities.project import Project


class IProjectRepository(ABC):
    @abstractmethod
    def create_project(self, project: Project) -> Project:
        pass

    @abstractmethod
    def get_project(self, project_id: int) -> Project | None:
        pass

    @abstractmethod
    def get_project_by_name(self, name: str) -> Project | None:
        pass

    @abstractmethod
    def get_projects(self) -> Sequence[Project]:
        pass

    @abstractmethod
    def delete_project(self, project: Project) -> Project:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass
