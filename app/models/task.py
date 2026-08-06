from pydantic import BaseModel

class Task(BaseModel):
    title: str
    priority : str
    completed: bool