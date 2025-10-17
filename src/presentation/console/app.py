from src.core.domain.entities.project import Project
from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.application.dtos.response_dto import ResponseDto
from src.presentation.console.program import project_contract


print('''Welcome to your Todo List program.
    1. Add project
    2. Add task
''')


command: int = 1

while command != 0:
    command: int = int(input('What do you want to do?'))

    if command == 1:
        name: str = input('Give your project a name:')
        add_project_dto: ProjectDtos.AddProjectDto = ProjectDtos.AddProjectDto(name)

        response: ResponseDto[Project] = project_contract.add_project(add_project_dto)
        if not response.success:
            print(f'Error: {response.message}')
        
        print(f'Your project created successfully: {response.result}')
    elif command == 2:
        response: ResponseDto[list[Project]] = project_contract.get_projects()
        if not response.success:
            print(f'Error: {response.message}')

        for project in response.result:
            print(project.name)
