from typing import Optional

from cassandra.cqlengine.management import sync_table
from fastapi import FastAPI

from todo.models import Task
from todo.db import connect_to_database, close_connection_to_database, get_db_client

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    await connect_to_database()
    await sync_table(Task)


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_connection_to_database()


@app.get("/")
def read_root():
    return {"msg": "Hello, World"}
