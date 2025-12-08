from collections.abc import Sequence
from fastapi import APIRouter, HTTPException

from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.i_use_cases.i_project_use_case import IProjectUseCase


class ProjectEndpoint:
   def __init__(self, project_use_case: IProjectUseCase):
      self.project_use_case = project_use_case
      self.router = APIRouter(prefix="/project", tags=["project"])

      self.router.add_api_route("/", self.add_project, methods=["POST"], response_model=ResponseDto[ProjectDtos.ProjectResponseDto])
      self.router.add_api_route("/{project_id}", self.get_project, methods=["GET"], response_model=ResponseDto[ProjectDtos.ProjectResponseDto])
      self.router.add_api_route("/", self.get_projects, methods=["GET"], response_model=ResponseDto[Sequence[ProjectDtos.ProjectResponseDto]])
      self.router.add_api_route("/", self.edit_project, methods=["PUT"], response_model=ResponseDto[ProjectDtos.ProjectResponseDto])
      self.router.add_api_route("/{name}", self.remove_project, methods=["DELETE"], response_model=ResponseDto[ProjectDtos.ProjectResponseDto])

   def add_project(self, add_project_dto: ProjectDtos.AddProjectDto) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
      response: ResponseDto[ProjectDtos.ProjectResponseDto] = self.project_use_case.add_project(add_project_dto)
      if not response.success:
         raise HTTPException(status_code=400, detail=response.message)
      
      return response.result

   def get_project(self, project_id: int) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
      response: ResponseDto[ProjectDtos.ProjectResponseDto] = self.project_use_case.get_project(project_id)
      if not response.success:
         raise HTTPException(status_code=404, detail=response.message)
      
      return response.result

   def get_projects(self) -> ResponseDto[Sequence[ProjectDtos.ProjectResponseDto]]:
      response: ResponseDto[Sequence[ProjectDtos.ProjectResponseDto]] = self.project_use_case.get_projects()
      if not response.success:
         raise HTTPException(status_code=400, detail=response.message)
      
      return response.result

   def edit_project(self, edit_project_dto: ProjectDtos.EditProjectDto) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
      response: ResponseDto[ProjectDtos.ProjectResponseDto] = self.project_use_case.edit_project(edit_project_dto)
      if not response.success:
         raise HTTPException(status_code=400, detail=response.message)
      
      return response.result

   def remove_project(self, name: str) -> ResponseDto[ProjectDtos.ProjectResponseDto]:
      response: ResponseDto[ProjectDtos.ProjectResponseDto] = self.project_use_case.remove_project(name)
      if not response.success:
         raise HTTPException(status_code=404, detail=response.message)
      
      return response.result
