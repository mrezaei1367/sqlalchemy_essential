from sqlalchemy import text
from db import engine
from db import SessionLocal


with engine.connect() as conn:
    stmt = text("SELECT cookie_name, quantity, unit_cost FROM cookies WHERE quantity > 50")
    result = conn.execute(stmt)

    for row in result:
        print(f"{row.cookie_name}: {row.quantity} pcs, unit cost ${row.unit_cost}")


with engine.connect() as conn:
    stmt = text("SELECT cookie_name, quantity, unit_cost FROM cookies WHERE unit_cost < :max_cost")
    result = conn.execute(stmt, {"max_cost": 0.5})

    for row in result:
        print(f"{row.cookie_name}: {row.quantity} pcs, unit cost ${row.unit_cost}")


with SessionLocal() as session:
    stmt = text("SELECT username, email_address FROM users WHERE username LIKE :prefix")
    result = session.execute(stmt, {"prefix": "a%"})

    for row in result:
        print(f"User: {row.username}, Email: {row.email_address}")


with SessionLocal() as session:
    # Insert a new cookie
    session.execute(
        text("INSERT INTO cookies (cookie_name, cookie_sku, quantity, unit_cost) VALUES (:name, :sku, :qty, :cost)"),
        {"name": "Lemon Cookie", "sku": "LC001", "qty": 100, "cost": 0.4}
    )

    # Update
    session.execute(
        text("UPDATE cookies SET quantity = quantity + :add_qty WHERE cookie_name = :name"),
        {"add_qty": 20, "name": "Lemon Cookie"}
    )

    # Delete
    session.execute(
        text("DELETE FROM cookies WHERE cookie_name = :name"),
        {"name": "Lemon Cookie"}
    )

    session.commit()
    print("Raw SQL operations done!")