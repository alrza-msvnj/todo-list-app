from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.presentation.api.endpoints.project_endpoint import ProjectEndpoint
from src.presentation.api.endpoints.task_endpoints import TaskEndpoint
from src.presentation.setup import project_use_case, task_use_case


app = FastAPI(title="Todo List API", version="1.0.0")


project_endpoints = ProjectEndpoint(project_use_case)
task_endpoints = TaskEndpoint(task_use_case)

app.include_router(project_endpoints.router)
app.include_router(task_endpoints.router)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
