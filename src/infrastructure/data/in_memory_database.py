from src.core.domain.entities.project import Project
from src.core.domain.entities.task import Task


class InMemoryDatabase:
    def __init__(self):
        self.projects: list[Project] = []
        self.tasks: list[Task] = []
