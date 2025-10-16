from src.core.application.contracts.project_contract import ProjectContract
from src.core.application.contracts.task_contract import TaskContract
from src.core.application.use_cases.project_use_case import ProjectUseCase
from src.core.application.use_cases.task_use_case import TaskUseCase
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.core.domain.i_repositories.i_task_repository import ITaskRepository
from src.infrastructure.data.in_memory_database import InMemoryDatabase
from src.infrastructure.repositories.project_repository import ProjectRepository
from src.infrastructure.repositories.task_repository import TaskRepository


db: InMemoryDatabase = InMemoryDatabase()

project_repository: IProjectRepository = ProjectRepository(db)
task_repository: ITaskRepository = TaskRepository(db)

project_contract: ProjectContract = ProjectUseCase(project_repository)
task_contract: TaskContract = TaskUseCase(task_repository)
