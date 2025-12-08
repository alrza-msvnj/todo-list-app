from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel


class TaskDtos:
    class TaskResponseDto(BaseModel):
        id: int
        project_id: int
        title: str
        description: str | None
        due_date: date | None
        status: Literal['todo', 'doing', 'done']
        closed_at: datetime | None
        created_at: datetime

    class AddTaskDto(BaseModel):
        project_name: str
        title: str
        description: str | None
        due_date: date | None

    class EditTaskDto(BaseModel):
        project_name: str
        title: str
        new_title: str | None
        new_description: str | None
        new_due_date: date | None
        new_status: Literal['todo', 'doing', 'done'] | None
