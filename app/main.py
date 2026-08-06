from fastapi import FastAPI
app = FastAPI()
from app.models.task import Task

@app.get("/")
def root():
    return {
        "message" : "Welcome to Taskflow AI Backend!"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id:int):
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
def create_task(task: Task):
    return {
        "message": "Task created successfully",
        "task": task
    }