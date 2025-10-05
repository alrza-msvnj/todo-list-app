from dataclasses import dataclass
from datetime import datetime


@dataclass
class Project:
    id: int
    name: str
    creation_timestamp: datetime
