# tests/test_joins.py
from sqlalchemy import select
from app.models import User, Order

def test_user_order_relationship(db_session):
    user = User(
        username="testuser",
        email_address="test@test.com",
        phone="123",
        password="pass"
    )
    db_session.add(user)
    db_session.commit()

    order = Order(user_id=user.user_id)
    db_session.add(order)
    db_session.commit()

    stmt = select(Order).where(Order.user_id == user.user_id)
    orders = db_session.execute(stmt).scalars().all()

    assert len(orders) == 1
