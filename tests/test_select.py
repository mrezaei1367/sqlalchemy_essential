# tests/test_select.py
from sqlalchemy import select
from app.models import Cookie

def test_select_cookie(db_session):
    cookie = Cookie(
        cookie_name="Select Cookie",
        cookie_sku="SC001",
        quantity=50,
        unit_cost=0.4
    )
    db_session.add(cookie)
    db_session.commit()

    stmt = select(Cookie).where(Cookie.cookie_name == "Select Cookie")
    result = db_session.execute(stmt).scalars().one()

    assert result.cookie_name == "Select Cookie"
    assert result.quantity == 50
