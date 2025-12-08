from collections.abc import Sequence
from fastapi import APIRouter, HTTPException

from src.core.application.dtos.response_dto import ResponseDto
from src.core.application.dtos.task_dtos import TaskDtos
from src.core.application.i_use_cases.i_task_use_case import ITaskUseCase


class TaskEndpoint:
   def __init__(self, task_use_case: ITaskUseCase):
      self.task_use_case = task_use_case
      self.router = APIRouter(prefix="/task", tags=["task"])

      self.router.add_api_route("/", self.add_task, methods=["POST"], response_model=TaskDtos.TaskResponseDto)
      self.router.add_api_route("/{task_id}", self.get_task, methods=["GET"], response_model=TaskDtos.TaskResponseDto)
      self.router.add_api_route("/", self.get_tasks, methods=["GET"], response_model=Sequence[TaskDtos.TaskResponseDto])
      self.router.add_api_route("/", self.edit_task, methods=["PUT"], response_model=TaskDtos.TaskResponseDto)
      self.router.add_api_route("/{name}", self.remove_task, methods=["DELETE"], response_model=TaskDtos.TaskResponseDto)

   def add_task(self, add_task_dto: TaskDtos.AddTaskDto) -> TaskDtos.TaskResponseDto:
      response: ResponseDto[TaskDtos.TaskResponseDto] = self.task_use_case.add_task(add_task_dto)
      if not response.success:
         raise HTTPException(status_code=400, detail=response.message)
      
      return response.result

   def get_task(self, task_id: int) -> TaskDtos.TaskResponseDto:
      response: ResponseDto[TaskDtos.TaskResponseDto] = self.task_use_case.get_task(task_id)
      if not response.success:
         raise HTTPException(status_code=404, detail=response.message)
      
      return response.result

   def get_tasks(self) -> Sequence[TaskDtos.TaskResponseDto]:
      response: ResponseDto[Sequence[TaskDtos.TaskResponseDto]] = self.task_use_case.get_tasks()
      if not response.success:
         raise HTTPException(status_code=400, detail=response.message)
      
      return response.result

   def edit_task(self, edit_task_dto: TaskDtos.EditTaskDto) -> TaskDtos.TaskResponseDto:
      response: ResponseDto[TaskDtos.TaskResponseDto] = self.task_use_case.edit_task(edit_task_dto)
      if not response.success:
         raise HTTPException(status_code=400, detail=response.message)
      
      return response.result

   def remove_task(self, project_name: str, title: str) -> TaskDtos.TaskResponseDto:
      response: ResponseDto[TaskDtos.TaskResponseDto] = self.task_use_case.remove_task(project_name, title)
      if not response.success:
         raise HTTPException(status_code=404, detail=response.message)
      
      return response.result
