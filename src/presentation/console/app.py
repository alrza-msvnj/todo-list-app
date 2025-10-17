from datetime import datetime

from src.core.application.dtos.task_dtos import TaskDtos
from src.core.domain.entities.project import Project
from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.application.dtos.response_dto import ResponseDto
from src.core.domain.entities.task import Task
from src.presentation.console.program import project_contract, task_contract


while True:
    command: int = int(input('''What do you want to do?
    1. Add project
    2. Add task
    3. Show projects
    4. Show tasks
    5. Remove project
    6. Remove task
    '''))

    if command == 0:
        break
    elif command == 1:
        name: str = input('Give your project a name:')
        add_project_dto: ProjectDtos.AddProjectDto = ProjectDtos.AddProjectDto(name)

        response: ResponseDto[Project] = project_contract.add_project(add_project_dto)
        if not response.success:
            print(f'Error: {response.message}')
        
        print(f'Your project created successfully: {response.result}')
    elif command == 2:
        print ('In which project you want to add your task?')

        response: ResponseDto[list[Project]] = project_contract.get_projects()
        for project in response.result:
            print(project.name)

        project_name: str = input()
        title: str = input('Give your task a name:')
        due_date: datetime | None = input('Give your task a due date (optional):')
        add_task_dto: TaskDtos.AddTaskDto = TaskDtos.AddTaskDto(project_name, title, due_date)

        response: ResponseDto[Task] = task_contract.add_task(add_task_dto)
        if not response.success:
            print(f'Error: {response.message}')
        
        print(f'Your task created successfully: {response.result}')
    elif command == 3:
        response: ResponseDto[list[Project]] = project_contract.get_projects()
        for project in response.result:
            print(project.name)
    elif command == 4:
        response: ResponseDto[list[Task]] = task_contract.get_tasks()
        for task in response.result:
            print(task.title)
    elif command == 5:
        response: ResponseDto[list[Project]] = project_contract.get_projects()
        for project in response.result:
            print(project.name)

        name: str = input('Enter project name to remove: ')

        response: ResponseDto[Project] = project_contract.remove_project(name)
        if not response.success:
            print(f'Error: {response.message}')

        print(f'Project {name} removed successfully.')
    elif command == 6:
        print ('In which project you want to remove your task?')

        response: ResponseDto[list[Project]] = project_contract.get_projects()
        for project in response.result:
            print(project.name)

        project_name: str = input()

        response: ResponseDto[list[Task]] = task_contract.get_tasks(project_name)
        for task in response.result:
            print(task.title)

        title: str = input('Enter task name to remove: ')

        response: ResponseDto[Project] = task_contract.remove_task(project_name, title)
        if not response.success:
            print(f'Error: {response.message}')

        print(f'Task {title} removed successfully.')
