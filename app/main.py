from fastapi import FastAPI
from uuid import uuid4, UUID
from fastapi import HTTPException
    
app = FastAPI()
from app.models.task import TaskCreate, Task, TaskUpdate

tasks = []

@app.get("/")
def root():
    return {
        "message" : "Welcome to Taskflow AI Backend!"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id:UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

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

@app.put("/tasks/{task_id}")
def update_task(task_id: UUID, task_update: TaskUpdate):
    for task in tasks:
        if task.id == task_id:
            task.title = task_update.title
            task.priority = task_update.priority
            task.completed = task_update.completed
            return {
                "message": "Task updated successfully",
                "task": task
            }
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {
                "message": "Task deleted successfully"
            }
    raise HTTPException(status_code=404, detail="Task not found")