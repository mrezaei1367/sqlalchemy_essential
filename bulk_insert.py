# bulk_insert.py
from db import SessionLocal, create_tables
from models import Cookie, User, Order, LineItem
from datetime import datetime

# Ensure tables exist
# create_tables()

with SessionLocal() as session:
    # ----------------------------
    # 1️⃣ Bulk insert cookies
    # ----------------------------
    cookies_list = [
        Cookie(cookie_name="Sugar Cookie", cookie_sku="SC001", quantity=120, unit_cost=0.35),
        Cookie(cookie_name="Double Chocolate", cookie_sku="DC001", quantity=80, unit_cost=0.6),
        Cookie(cookie_name="Macadamia Nut", cookie_sku="MN001", quantity=60, unit_cost=0.7),
    ]
    session.add_all(cookies_list)

    # ----------------------------
    # 2️⃣ Bulk insert users
    # ----------------------------
    users_list = [
        User(username="charlie", email_address="charlie@example.com", phone="555-111", password="pwd789"),
        User(username="dave", email_address="dave@example.com", phone="555-222", password="pwd012"),
    ]
    session.add_all(users_list)

    # ----------------------------
    # 3️⃣ Bulk insert orders
    # ----------------------------
    orders_list = [
        Order(user_id=3),  # charlie
        Order(user_id=4),  # dave
    ]
    session.add_all(orders_list)

    # ----------------------------
    # 4️⃣ Bulk insert line items
    # ----------------------------
    line_items_list = [
        LineItem(order_id=3, cookie_id=4, quantity=10, extended_cost=10 * 0.35),
        LineItem(order_id=3, cookie_id=5, quantity=5, extended_cost=5 * 0.6),
        LineItem(order_id=4, cookie_id=6, quantity=7, extended_cost=7 * 0.7),
    ]
    session.add_all(line_items_list)

    # ----------------------------
    # Commit all at once
    # ----------------------------
    session.commit()
    print("Bulk insert completed successfully!")
