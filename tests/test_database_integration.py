# tests/test_database_integration.py
import pytest
from tests import database


@pytest.fixture
def db_connection():
    conn = database.create_connection()
    database.init_db(conn)
    yield conn
    conn.close()


def test_add_and_get_user(db_connection):
    database.add_user(db_connection, "Alice")
    users = database.get_users(db_connection)
    print(users)
    assert len(users) == 1
    assert users[0][0] == 1
    assert users[0][1] == "Alice"
