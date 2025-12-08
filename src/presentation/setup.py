import time
import schedule
from sqlalchemy.orm import Session

from src.core.application.i_use_cases.i_project_use_case import IProjectUseCase
from src.core.application.i_use_cases.i_task_use_case import ITaskUseCase
from src.core.application.use_cases.project_use_case import ProjectUseCase
from src.core.application.use_cases.task_use_case import TaskUseCase
from src.core.application.jobs.close_overdue_tasks_job import CloseOverdueTasksJob
from src.core.domain.i_repositories.i_project_repository import IProjectRepository
from src.core.domain.i_repositories.i_task_repository import ITaskRepository
from src.infrastructure.persistence.data.session import SessionLocal
from src.infrastructure.persistence.repositories.project_repository import ProjectRepository
from src.infrastructure.persistence.repositories.task_repository import TaskRepository


db: Session = SessionLocal()

project_repository: IProjectRepository = ProjectRepository(db)
task_repository: ITaskRepository = TaskRepository(db)


project_use_case: IProjectUseCase = ProjectUseCase(project_repository, task_repository)
task_use_case: ITaskUseCase = TaskUseCase(task_repository, project_repository)

# close_overdue_tasks_job: CloseOverdueTasksJob = CloseOverdueTasksJob(task_repository)
# schedule.every(10).seconds.do(close_overdue_tasks_job.execute)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
