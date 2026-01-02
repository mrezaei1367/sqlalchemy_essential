# tests/test_tables.py
from sqlalchemy import inspect

def test_tables_exist(db_session):
    inspector = inspect(db_session.bind)

    tables = inspector.get_table_names()

    assert "cookies" in tables
    assert "users" in tables
    assert "orders" in tables
    assert "line_items" in tables
