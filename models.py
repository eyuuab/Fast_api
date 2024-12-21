# structure of the to-do task
from pydantic import BaseModel

#task model 
class Task(BaseModel):
    title: str 
    description: str | None = None
    completed: bool = False
