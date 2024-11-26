from fastapi import FastAPI, HTTPException
from sqlalchemy import select

from depencies import SessionDependency
from schemas import Login, TaskCreate
from models import Users, Tasks

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello"}


@app.post("/login")
async def login(session: SessionDependency, login_data: Login):
    user = Users(**login_data.dict())
    session.add(user)
    try:
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существет")

    return {"name": user.name, "password": user.password}


@app.post("/tasks")
async def create_task(session: SessionDependency, task_data: TaskCreate):
    task = Tasks(**task_data.dict())
    session.add(task)

    try:
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Ошибка при добавлении задачи")

    return {"task": task.task, "done": task.done}


# @app.get("/tasks")
# async def get_tasks(session: SessionDependency, task_data: TaskCreate):
#     task = Tasks(**task_data.dict())
#     tasks = session.exec(select(task)).all()
#     return {"message": "Hello World"}
