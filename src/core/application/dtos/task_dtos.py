from dataclasses import dataclass
from datetime import datetime
from typing import Literal


class TaskDtos:
    @dataclass
    class AddTaskDto:
        project_name: str
        title: str
        description: str | None
        due_date: datetime | None

    @dataclass
    class EditTaskDto:
        project_name: str
        title: str
        new_title: str | None
        new_description: str | None
        new_due_date: datetime | None
        new_status: Literal['todo', 'doing', 'done'] | None
