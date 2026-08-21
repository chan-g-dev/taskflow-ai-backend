from uuid import UUID
from pydantic import BaseModel

class Task(BaseModel):
    id : UUID
    title: str
    priority : str
    completed: bool

class TaskCreate(BaseModel):
    title: str
    priority : str
    completed: bool