# chaining_examples.py
from sqlalchemy import select, func
from db import SessionLocal
from models import Cookie, User, Order, LineItem

with SessionLocal() as session:

    # ----------------------------
    # Example 1: Chaining filters and joins
    # ----------------------------
    stmt = (
        select(
            User.username,
            Cookie.cookie_name,
            LineItem.quantity,
            LineItem.extended_cost
        )
        .join(Order, Order.user_id == User.user_id)
        .join(LineItem, LineItem.order_id == Order.order_id)
        .join(Cookie, LineItem.cookie_id == Cookie.cookie_id)
        .where(LineItem.quantity > 5)
        .order_by(User.username, Cookie.cookie_name)
    )

    print("=== Users with line items quantity > 5 ===")
    result = session.execute(stmt)
    for row in result:
        print(f"{row.username} bought {row.quantity}x {row.cookie_name} costing {row.extended_cost}")


    # ----------------------------
    # Example 2: Chaining aggregates
    # ----------------------------
    stmt2 = (
        select(
            User.username,
            func.sum(LineItem.extended_cost).label("total_spent")
        )
        .join(Order, Order.user_id == User.user_id)
        .join(LineItem, LineItem.order_id == Order.order_id)
        .group_by(User.username)
        .having(func.sum(LineItem.extended_cost) > 5)  # only users who spent more than $5
        .order_by(func.sum(LineItem.extended_cost).desc())
    )

    print("\n=== Users who spent more than $5 ===")
    result2 = session.execute(stmt2)
    for row in result2:
        print(f"{row.username} spent ${row.total_spent:.2f}")


    # ----------------------------
    # Example 3: Combining filters, joins, aggregates, and labels
    # ----------------------------
    stmt3 = (
        select(
            Cookie.cookie_name,
            func.count(LineItem.line_items_id).label("times_ordered"),
            func.sum(LineItem.extended_cost).label("total_revenue")
        )
        .join(LineItem, LineItem.cookie_id == Cookie.cookie_id)
        .group_by(Cookie.cookie_name)
        .having(func.sum(LineItem.extended_cost) > 1)
        .order_by(func.sum(LineItem.extended_cost).desc())
    )

    print("\n=== Cookies sold more than $1 in revenue ===")
    result3 = session.execute(stmt3)
    for row in result3:
        print(f"{row.cookie_name} was ordered {row.times_ordered} times, total revenue ${row.total_revenue:.2f}")
