from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.domain.entities.project import Project


class ProjectFactory:
   @staticmethod
   def map_to_project_response_dto(project: Project) -> ProjectDtos.ProjectResponseDto:
      project_response_dto: ProjectDtos.ProjectResponseDto = ProjectDtos.ProjectResponseDto(
         id=project.id,
         name=project.name,
         description=project.description,
         created_at=project.created_at
      )

      return project_response_dto
