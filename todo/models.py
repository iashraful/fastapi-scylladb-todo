from uuid import UUID

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Task(Model):
    id: UUID = columns.UUID(primary_key=True)
    title: str = columns.Text(min_length=0, max_length=255)
    is_compleated = columns.Boolean(default=False)

    