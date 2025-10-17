from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Literal


@dataclass
class Task:
    id: int
    project_id: int
    title: str
    due_date: datetime | None
    status: Literal['todo', 'doing', 'done']
    creation_timestamp: datetime

    def __init__(self, project_id: int, title: str, due_date: datetime | None = None):
        self.project_id = project_id
        self.title = title
        self.due_date = due_date
        self.status = 'todo'
        self.creation_timestamp = datetime.now(timezone.utc)
