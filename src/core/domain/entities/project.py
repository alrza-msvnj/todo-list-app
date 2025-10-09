from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Project:
    id: int
    name: str
    creation_timestamp: datetime
    
    def __init__(self, name: str):
        self.name = name
        self.creation_timestamp = datetime.now(timezone.utc)
