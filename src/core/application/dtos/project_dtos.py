from dataclasses import dataclass


class ProjectDtos:
    @dataclass
    class AddProjectDto:
        name: str

    @dataclass
    class EditProjectDto:
        id: int
        name: str
