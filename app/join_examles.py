# join_examples.py
from sqlalchemy import select, func
from db import SessionLocal
from models import Cookie, User, Order, LineItem

with SessionLocal() as session:

    # ----------------------------
    # 1️⃣ Join Orders with Users
    # ----------------------------
    stmt = (
        select(Order.order_id, User.username)
        .join(User, User.user_id == Order.user_id)
    )

    print("=== Orders with Users ===")
    result = session.execute(stmt)
    for row in result:
        print(f"Order {row.order_id} belongs to {row.username}")


    # ----------------------------
    # 2️⃣ Join LineItems with Cookies and Orders
    # ----------------------------
    stmt = (
        select(
            LineItem.line_item_id,
            Cookie.cookie_name,
            LineItem.quantity,
            LineItem.extended_cost,
            Order.order_id
        )
        .join(Cookie, Cookie.cookie_id == LineItem.cookie_id)
        .join(Order, Order.order_id == LineItem.order_id)
    )

    print("\n=== Line Items with Cookies and Orders ===")
    result = session.execute(stmt)
    for row in result:
        print(
            f"LineItem {row.line_item_id}: {row.quantity}x {row.cookie_name}, "
            f"cost {row.extended_cost}, Order {row.order_id}"
        )

    # ----------------------------
    # 3️⃣ Aggregate join: Total spent by each user
    # ----------------------------
    stmt = (
        select(
            User.username,
            func.sum(LineItem.extended_cost).label("total_spent")
        )
        .join(Order, Order.user_id == User.user_id)
        .join(LineItem, LineItem.order_id == Order.order_id)
        .group_by(User.user_id)
    )

    print("\n=== Total spent by each user ===")
    result = session.execute(stmt)
    for row in result:
        print(f"{row.username} spent {row.total_spent}")
    
    # ----------------------------
    # 4 selectfrom
    # ----------------------------
    stmt = (
        select(
            User.username,
            Cookie.cookie_name,
            LineItem.quantity,
            LineItem.extended_cost
        ).join(Cookie, Cookie.cookie_id == LineItem.cookie_id)
            .join(Order, Order.order_id == LineItem.order_id)
            .join(User, User.user_id == Order.user_id)
        )

    result = session.execute(stmt)
    for row in result:
        print(f"{row.username} ordered {row.quantity}x {row.cookie_name} = {row.extended_cost}")
   
    #another way is 
    join_stmt = LineItem.__table__.join(
        Order.__table__, LineItem.order_id == Order.order_id
    ).join(
        User.__table__, Order.user_id == User.user_id
    ).join(
        Cookie.__table__, LineItem.cookie_id == Cookie.cookie_id
    )

    stmt = select(
        User.username,
        Cookie.cookie_name,
        LineItem.quantity,
        LineItem.extended_cost
    ).select_from(join_stmt)

    result = session.execute(stmt)
    for row in result:
        print(f"{row.username} ordered {row.quantity}x {row.cookie_name} = {row.extended_cost}")