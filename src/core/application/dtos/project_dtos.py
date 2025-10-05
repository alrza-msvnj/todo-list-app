from typing import TypedDict


class ProjectDtos:
    class AddProjectDto(TypedDict):
        name: str

    class EditProjectDto(TypedDict):
        id: int
        name: str
