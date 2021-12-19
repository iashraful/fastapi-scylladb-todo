import os

from cassandra.cluster import Cluster, Session

_client: Session = None


async def get_db_client():
    return _client


async def connect_to_database():
    _hosts = [os.environ.get("DB_HOST", "127.0.0.1")]
    _port = os.environ.get("DB_PORT", 9042)
    cluster = Cluster(contact_points=_hosts, port=_port)

    global _client
    _client = cluster.connect(keyspace="todo_keyspace")


async def close_connection_to_database():
    _client.shutdown()
