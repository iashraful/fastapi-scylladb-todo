from typing import List
from uuid import UUID
from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: UUID
    title: str
    description: str
    is_completed: bool = False


class TaskCreateSchema(BaseModel):
    title: str
    description: str


class TaskUpdateSchema(BaseModel):
    title: str
    description: str
    is_completed: bool


class TaskCompletedSchema(BaseModel):
    is_completed: bool


class TaskListResponse(BaseModel):
    success: bool = True
    data: List[TaskSchema]


class TaskResponse(BaseModel):
    success: bool = True
    data: TaskSchema
