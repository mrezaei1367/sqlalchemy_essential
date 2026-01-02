# update_data.py
from sqlalchemy import select, update
from db import SessionLocal
from models import Cookie, User, Order, LineItem

with SessionLocal() as session:
    # ----------------------------
    # 1️⃣ Update a cookie's quantity
    # ----------------------------
    stmt = (
        update(Cookie)
        .where(Cookie.cookie_name == "Chocolate Chip")
        .values(quantity=150, unit_cost=0.55)
    )
    session.execute(stmt)
    
    # ----------------------------
    # 2️⃣ Update a user's phone
    # ----------------------------
    stmt = (
        update(User)
        .where(User.username == "alice")
        .values(phone="111-222-333")
    )
    session.execute(stmt)

    # ----------------------------
    # 3️⃣ Update an order (assign it to another user)
    # ----------------------------
    stmt = (
        update(Order)
        .where(Order.order_id == 2)  # Bob's order
        .values(user_id=1)            # Assign to Alice
    )
    session.execute(stmt)

    # ----------------------------
    # 4️⃣ Update line item quantity and recalc extended_cost
    # ----------------------------
    stmt = (
        update(LineItem)
        .where(LineItem.line_items_id == 3)
        .values(quantity=5, extended_cost=5 * 0.45)  # assuming unit_cost = 0.45
    )
    session.execute(stmt)

    # ----------------------------
    # Commit all changes
    # ----------------------------
    session.commit()
    print("Data updated successfully!")
