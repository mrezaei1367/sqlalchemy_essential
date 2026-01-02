# tests/test_delete.py
from sqlalchemy import select
from app.models import Cookie

def test_delete_cookie(db_session):
    cookie = Cookie(
        cookie_name="Delete Cookie",
        cookie_sku="DC001",
        quantity=10,
        unit_cost=0.2
    )
    db_session.add(cookie)
    db_session.commit()

    db_session.delete(cookie)
    db_session.commit()

    stmt = select(Cookie).where(Cookie.cookie_name == "Delete Cookie")
    result = db_session.execute(stmt).scalars().all()

    assert result == []
