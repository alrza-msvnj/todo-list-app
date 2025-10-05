from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass
class Task:
    id: int
    title: str
    due_date: datetime
    status: Literal['todo', 'doing', 'done']
    creation_timestamp: datetime
