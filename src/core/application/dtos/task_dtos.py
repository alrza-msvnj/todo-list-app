from dataclasses import dataclass
from datetime import datetime
from typing import Literal


class TaskDtos:
    @dataclass
    class AddTaskDto:
        project_name: str
        title: str
        due_date: datetime | None

    @dataclass
    class EditTaskDto:
        id: int
        title: str | None
        due_date: datetime | None
        status: Literal['todo', 'doing', 'done'] | None
