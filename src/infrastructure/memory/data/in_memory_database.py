from src.core.domain.entities.project import Project
from src.core.domain.entities.task import Task


class InMemoryDatabase:
    def __init__(self):
        self.projects: list[Project] = []
        self.tasks: list[Task] = []
        self.project_id_counter = 0
        self.task_id_counter = 0
    
    def create_project(self, project: Project) -> Project:
        self.project_id_counter += 1
        project.id = self.project_id_counter

        self.projects.append(project)

        return project
    
    def create_task(self, task: Task) -> Task:
        self.task_id_counter += 1
        task.id = self.task_id_counter

        self.tasks.append(task)

        return task
