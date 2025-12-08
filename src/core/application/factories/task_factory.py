from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.application.dtos.task_dtos import TaskDtos
from src.core.domain.entities.project import Project
from src.core.domain.entities.task import Task


class TaskFactory:
   @staticmethod
   def map_to_task_response_dto(task: Task) -> TaskDtos.TaskResponseDto:
      task_response_dto: TaskDtos.TaskResponseDto = TaskDtos.TaskResponseDto(
         id=task.id,
         project_id=task.project_id,
         title=task.title,
         description=task.description,
         due_date=task.due_date,
         status=task.status,
         closed_at=task.closed_at,
         created_at=task.created_at
      )

      return task_response_dto
