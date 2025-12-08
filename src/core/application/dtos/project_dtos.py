from datetime import datetime

from pydantic import BaseModel


class ProjectDtos:
    class ProjectResponseDto(BaseModel):
        id: int
        name: str
        description: str | None = None
        created_at: datetime

    class AddProjectDto(BaseModel):
        name: str
        description: str | None = None

    class EditProjectDto(BaseModel):
        name: str
        new_name: str | None = None
        new_description: str | None = None
