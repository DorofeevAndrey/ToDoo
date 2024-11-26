from pydantic import BaseModel


class Login(BaseModel):
    name: str
    password: str


class TaskCreate(BaseModel):
    task: str
    done: bool = False
