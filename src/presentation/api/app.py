from fastapi import FastAPI

from src.presentation.api.endpoints.project_endpoint import ProjectEndpoint
from src.presentation.api.endpoints.task_endpoints import TaskEndpoint
from src.presentation.setup import project_use_case, task_use_case


app = FastAPI()


project_endpoints = ProjectEndpoint(project_use_case)
task_endpoints = TaskEndpoint(task_use_case)

app.include_router(project_endpoints.router)
app.include_router(task_endpoints.router)
