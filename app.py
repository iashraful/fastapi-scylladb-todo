from typing import Optional

import uvicorn
from cassandra.cqlengine.connection import register_connection, set_default_connection
from cassandra.cqlengine.management import sync_table
from fastapi import FastAPI

from todo.db import close_connection_to_database, connect_to_database, get_db_client
from todo.models import Task
from todo.routes import todo_router

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    await connect_to_database()
    conn = await get_db_client()
    register_connection(str(conn), session=conn)
    set_default_connection(str(conn))
    sync_table(Task)


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_connection_to_database()


@app.get("/")
def read_root():
    return {"msg": "Hello, World"}


app.include_router(todo_router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7001, reload=True, access_log=True)
