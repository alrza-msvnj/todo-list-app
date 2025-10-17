from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Project:
    id: int
    name: str
    description: str | None
    creation_timestamp: datetime
    
    def __init__(self, name: str, description: str | None = None):
        self.name = name
        self.description = description
        self.creation_timestamp = datetime.now(timezone.utc)
