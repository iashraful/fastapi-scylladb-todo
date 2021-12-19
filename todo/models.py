from uuid import UUID

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Task(Model):
    __table_name__ = "tasks"
    __keyspace__ = "todo_keyspace"

    id = columns.UUID(primary_key=True)
    title = columns.Text(min_length=3, max_length=255)
    description = columns.Text(min_length=0, max_length=512)
    is_completed = columns.Boolean(default=False)
