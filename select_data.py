# select_data.py
from db import SessionLocal
from models import Cookie, User, Order, LineItem
from sqlalchemy.orm import joinedload
from sqlalchemy import select, func, cast


session = SessionLocal()

print("=== Cookies ===")
for cookie in session.query(Cookie).all():
    print(cookie.cookie_id, cookie.cookie_name, cookie.cookie_sku, cookie.quantity, cookie.unit_cost)

print("\n=== Users ===")
for user in session.query(User).all():
    print(user.user_id, user.username, user.email_address)

print("\n=== Orders ===")
for order in session.query(Order).all():
    print(order.order_id, order.user_id)

print("\n=== Line Items ===")
for item in session.query(LineItem).all():
    print(item.line_items_id, item.order_id, item.cookie_id, item.quantity, item.extended_cost)

# Optional: join tables to show order details
print("\n=== Order Details ===")
results = session.query(User.username, Cookie.cookie_name, LineItem.quantity, LineItem.extended_cost)\
    .join(Order, Order.user_id == User.user_id)\
    .join(LineItem, LineItem.order_id == Order.order_id)\
    .join(Cookie, Cookie.cookie_id == LineItem.cookie_id)\
    .all()

for r in results:
    print(r)

session.close()

stmt = select(
    Cookie.cookie_name,
    (Cookie.quantity * Cookie.unit_cost).label("total_value")
).where(Cookie.quantity > 50)
