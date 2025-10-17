from dataclasses import dataclass


class ProjectDtos:
    @dataclass
    class AddProjectDto:
        name: str
        description: str | None

    @dataclass
    class EditProjectDto:
        name: str
        new_name: str | None
        new_description: str | None
