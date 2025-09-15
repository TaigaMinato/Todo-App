from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    done: bool = False


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
