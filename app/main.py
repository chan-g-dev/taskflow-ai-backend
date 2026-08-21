from fastapi import FastAPI
from uuid import uuid4, UUID

app = FastAPI()
from app.models.task import TaskCreate, Task

tasks = []

@app.get("/")
def root():
    return {
        "message" : "Welcome to Taskflow AI Backend!"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id:UUID):
    return {
        "task_id":task_id,
        "message":f"Fetching task {task_id}"
    }

@app.get("/search")
def search_tasks(priority: str, completed : bool):
    return{
        "priority": priority,
        "completed": completed,
    }

@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = Task(
        id=uuid4(),
        title=task.title,
        priority=task.priority,
        completed=task.completed
    )
    tasks.append(new_task)
    return {
        "message": "Task created successfully",
        "task": new_task
    }

@app.get("/tasks")
def get_tasks():
    return {
        "tasks" : tasks
    }