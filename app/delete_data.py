# delete_data.py
from sqlalchemy import delete
from db import SessionLocal
from models import Cookie, User, Order, LineItem

with SessionLocal() as session:

    # ----------------------------
    # 1️⃣ Delete a cookie by name
    # ----------------------------
    stmt = delete(Cookie).where(Cookie.cookie_name == "Peanut Butter")
    session.execute(stmt)

    # ----------------------------
    # 2️⃣ Delete a user by username
    # ----------------------------
    stmt = delete(User).where(User.username == "bob")
    session.execute(stmt)

    # ----------------------------
    # 3️⃣ Delete an order by order_id
    # ----------------------------
    stmt = delete(Order).where(Order.order_id == 2)
    session.execute(stmt)

    # ----------------------------
    # 4️⃣ Delete a line item by ID
    # ----------------------------
    stmt = delete(LineItem).where(LineItem.line_item_id == 1)
    session.execute(stmt)

    # ----------------------------
    # Commit all deletions
    # ----------------------------
    session.commit()
    print("Data deleted successfully!")
