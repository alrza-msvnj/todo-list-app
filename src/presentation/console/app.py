from datetime import datetime

from src.core.application.dtos.task_dtos import TaskDtos
from src.core.domain.entities.project import Project
from src.core.application.dtos.project_dtos import ProjectDtos
from src.core.application.dtos.response_dto import ResponseDto
from src.core.domain.entities.task import Task
from src.presentation.setup import i_project_use_case, i_task_use_case


while True:
    command: int = int(input('''What do you want to do?
    1. Add project
    2. Add task
    3. Show projects
    4. Show project tasks
    5. Edit task
    6. Remove project
    7. Remove task
    '''))

    if command == 0:
        break
    # Add project
    elif command == 1:
        name: str = input('Give your project a name:')
        description: str | None = input('Give your project a description (optional):')
        add_project_dto: ProjectDtos.AddProjectDto = ProjectDtos.AddProjectDto(name, description)

        response: ResponseDto[Project] = i_project_use_case.add_project(add_project_dto)
        if not response.success:
            print(f'Error: {response.message}')
        
        print('Project created successfully.')
    # Add task
    elif command == 2:
        project_name: str = input('Enter the project name in which you want to add your task: ')
        title: str = input('Give your task a name:')
        description: str | None = input('Give your task a description (optional):') or None
        due_date: datetime | None = input('Give your task a due date (year-month-day) (optional):') or None
        add_task_dto: TaskDtos.AddTaskDto = TaskDtos.AddTaskDto(project_name, title, description, due_date)

        response: ResponseDto[Task] = i_task_use_case.add_task(add_task_dto)
        if not response.success:
            print(f'Error: {response.message}')
        
        print('Task created successfully.')
    # Show projects
    elif command == 3:
        response: ResponseDto[list[Project]] = i_project_use_case.get_projects()
        if len(response.result) == 0:
            print('There are no projects.')

        for project in response.result:
            print(f'''
                  Id: {project.id}
                  Name: {project.name}
                  Description: {project.description}
                  ''')
    # Show project tasks
    elif command == 4:
        project_name: str = input('Enter a project name to see its related tasks: ')

        response: ResponseDto[list[Task]] = i_task_use_case.get_tasks(project_name)
        if len(response.result) == 0:
            print('There are no tasks for this project.')

        for task in response.result:
            print(f'''
                  Id: {task.id}
                  Title: {task.title}
                  Description: {task.description}
                  Due Date: {task.due_date}
                  Status: {task.status}
                  ''')
    # Edit task
    elif command == 5:
        project_name: str = input('Enter the project name of the task: ')
        title: str = input('Enter the task name: ')
        new_title: str | None = input('Enter the new task name (optional): ')
        new_description: str | None = input('Enter the new task description (optional): ')
        new_due_date: str | None = input('Enter the new task due date (year-month-day) (optional): ')
        new_status: str | None = input('Enter the new task status (optional): ')

        edit_task_dto: TaskDtos.EditTaskDto = TaskDtos.EditTaskDto(project_name, title, new_title, new_description, new_due_date, new_status)

        response: ResponseDto[Project] = i_task_use_case.edit_task(edit_task_dto)
        if not response.success:
            print(f'Error: {response.message}')

        print('Task edited successfully.')
    # Remove project
    elif command == 6:
        name: str = input('Enter project name to remove: ')

        response: ResponseDto[Project] = i_project_use_case.remove_project(name)
        if not response.success:
            print(f'Error: {response.message}')

        print('Project removed successfully.')
    # Remove task
    elif command == 7:
        project_name: str = input('Enter the project name of the task: ')
        title: str = input('Enter the task title: ')

        response: ResponseDto[Project] = i_task_use_case.remove_task(project_name, title)
        if not response.success:
            print(f'Error: {response.message}')

        print('Task removed successfully.')
