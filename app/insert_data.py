# insert_data.py
from db import SessionLocal, create_tables
from models import Cookie, User, Order, LineItem

# 1. Create tables if they don't exist
create_tables()

# 2. Open a session
session = SessionLocal()

# 3. Insert cookies
cookies = [
    Cookie(cookie_name="Chocolate Chip", cookie_sku="CC001", quantity=100, unit_cost=0.5),
    Cookie(cookie_name="Oatmeal Raisin", cookie_sku="OR001", quantity=50, unit_cost=0.4),
    Cookie(cookie_name="Peanut Butter", cookie_sku="PB001", quantity=75, unit_cost=0.45),
]
session.add_all(cookies)

# 4. Insert users
users = [
    User(username="alice", email_address="alice@example.com", phone="123-456", password="pwd123"),
    User(username="bob", email_address="bob@example.com", phone="987-654", password="pwd456")
]
session.add_all(users)

session.commit()  # commit cookies and users

# 5. Insert orders
orders = [
    Order(user_id=1),  # Alice
    Order(user_id=2)   # Bob
]
session.add_all(orders)
session.commit()

# 6. Insert line items
line_items = [
    LineItem(order_id=1, cookie_id=1, quantity=2, extended_cost=1.0),
    LineItem(order_id=1, cookie_id=2, quantity=1, extended_cost=0.4),
    LineItem(order_id=2, cookie_id=3, quantity=3, extended_cost=1.35)
]
session.add_all(line_items)
session.commit()

session.close()
print("Data inserted successfully!")
