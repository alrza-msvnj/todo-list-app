from core.domain.entities.project import Project
from core.domain.entities.task import Task


class InMemoryDatabase:
    projects: list[Project] = []
    tasks: list[Task] = []
