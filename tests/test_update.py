# tests/test_update.py
from sqlalchemy import select
from app.models import Cookie

def test_update_cookie(db_session):
    cookie = Cookie(
        cookie_name="Update Cookie",
        cookie_sku="UC001",
        quantity=20,
        unit_cost=0.3
    )
    db_session.add(cookie)
    db_session.commit()

    cookie.quantity = 99
    db_session.commit()

    stmt = select(Cookie).where(Cookie.cookie_name == "Update Cookie")
    updated = db_session.execute(stmt).scalars().one()

    assert updated.quantity == 99
