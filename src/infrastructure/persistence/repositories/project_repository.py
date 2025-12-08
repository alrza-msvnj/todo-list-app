from collections.abc import Sequence

from sqlalchemy.orm import Session
from sqlalchemy import select

from src.core.domain.entities.project import Project
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.infrastructure.persistence.data.session import SessionLocal


class ProjectRepository(IProjectRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project: Project) -> Project:
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def get_project(self, project_id: int) -> Project | None:
        return self.db.get(Project, project_id)
    
    def get_project_by_name(self, name: str) -> Project | None:
        query = select(Project).where(Project.name == name)

        return self.db.scalar(query)

    def get_projects(self) -> Sequence[Project]:
        query = select(Project)

        return self.db.scalars(query).all()

    def delete_project(self, project: Project) -> Project:
        self.db.delete(project)
        self.db.commit()

        return project
