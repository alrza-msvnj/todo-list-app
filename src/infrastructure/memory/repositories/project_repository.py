from collections.abc import Sequence

from src.core.domain.entities.project import Project
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.infrastructure.data.in_memory_database import InMemoryDatabase


class ProjectRepository(IProjectRepository):
    def __init__(self, in_memory_database: InMemoryDatabase):
        self.db = in_memory_database

    def create_project(self, project: Project) -> Project:
        return self.db.create_project(project)

    def get_project(self, project_id: int) -> Project | None:
        for project in self.db.projects:
            if project.id == project_id:
                return project
        
        return None
    
    def get_project_by_name(self, name: str) -> Project | None:
        for project in self.db.projects:
            if project.name == name:
                return project
        
        return None

    def get_projects(self) -> Sequence[Project]:
        return self.db.projects

    def delete_project(self, project: Project) -> Project:
        self.db.projects.remove(project)

        return project
