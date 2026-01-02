# groupby_examples.py
from sqlalchemy import select, func
from db import SessionLocal
from models import Cookie, User, Order, LineItem

with SessionLocal() as session:

    # ----------------------------
    # 1️⃣ Total quantity per cookie
    # ----------------------------
    stmt = (
        select(
            Cookie.cookie_name,
            func.sum(LineItem.quantity).label("total_sold")
        )
        .join(LineItem, LineItem.cookie_id == Cookie.cookie_id)
        .group_by(Cookie.cookie_name)
    )

    print("=== Total quantity sold per cookie ===")
    result = session.execute(stmt)
    for row in result:
        print(f"{row.cookie_name}: {row.total_sold} pcs sold")


    # ----------------------------
    # 2️⃣ Total spent per user
    # ----------------------------
    stmt = (
        select(
            User.username,
            func.sum(LineItem.extended_cost).label("total_spent")
        )
        .join(Order, Order.user_id == User.user_id)
        .join(LineItem, LineItem.order_id == Order.order_id)
        .group_by(User.username)
    )

    print("\n=== Total spent per user ===")
    result = session.execute(stmt)
    for row in result:
        print(f"{row.username} spent ${row.total_spent:.2f}")


    # ----------------------------
    # 3️⃣ Count of orders per user
    # ----------------------------
    stmt = (
        select(
            User.username,
            func.count(Order.order_id).label("num_orders")
        )
        .join(Order, Order.user_id == User.user_id)
        .group_by(User.username)
    )

    print("\n=== Number of orders per user ===")
    result = session.execute(stmt)
    for row in result:
        print(f"{row.username} has {row.num_orders} orders")
