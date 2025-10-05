from datetime import datetime
from typing import Literal, TypedDict


class TaskDtos:
    class AddTaskDto(TypedDict):
        title: str
        due_date: datetime | None

    class EditTaskDto(TypedDict):
        id: int
        title: str | None
        due_date: datetime | None
        status: Literal['todo', 'doing', 'done'] | None
