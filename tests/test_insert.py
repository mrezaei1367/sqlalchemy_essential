# tests/test_insert.py
from app.models import Cookie

def test_insert_cookie(db_session):
    cookie = Cookie(
        cookie_name="Test Cookie",
        cookie_sku="TC001",
        quantity=100,
        unit_cost=0.5
    )

    db_session.add(cookie)
    db_session.commit()

    assert cookie.cookie_id is not None
