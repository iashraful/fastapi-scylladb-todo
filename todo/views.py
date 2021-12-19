import uuid

from fastapi import Depends

from todo.db import DBSession, get_db_client
from todo.models import Task
from todo.schema import (
    TaskCreateSchema,
    TaskListResponse,
    TaskResponse,
    TaskSchema,
    TaskUpdateSchema,
)


class TaskView:
    @staticmethod
    async def list(db: DBSession = Depends(get_db_client)) -> TaskListResponse:
        result = Task.objects()
        return [TaskSchema(**r) for r in result]

    @staticmethod
    async def create(task: TaskCreateSchema, db: DBSession = Depends(get_db_client)):
        result = Task.create(
            id=uuid.uuid4(), title=task.title, description=task.description
        )
        return TaskResponse(data=TaskSchema(**result))

    @staticmethod
    async def update(
        id: uuid.UUID, task: TaskUpdateSchema, db: DBSession = Depends(get_db_client)
    ) -> TaskResponse:
        instance = Task.objects(id=id).first()
        result = instance.update(
            title=task.title,
            description=task.description,
            is_completed=task.is_completed,
        )
        return TaskResponse(data=TaskSchema(*result))
