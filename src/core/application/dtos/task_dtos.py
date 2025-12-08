from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel


class TaskDtos:
    class TaskResponseDto(BaseModel):
        id: int
        project_id: int
        title: str
        description: str | None = None
        due_date: date | None = None
        status: Literal['todo', 'doing', 'done']
        closed_at: datetime | None = None
        created_at: datetime

    class AddTaskDto(BaseModel):
        project_name: str
        title: str
        description: str | None = None
        due_date: date | None = None

    class EditTaskDto(BaseModel):
        project_name: str
        title: str
        new_title: str | None = None
        new_description: str | None = None
        new_due_date: date | None = None
        new_status: Literal['todo', 'doing', 'done'] | None = None
