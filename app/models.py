# models.py
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from datetime import datetime
from app.db import Base

class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer)
    unit_cost = Column(Numeric(12, 2))

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    customer_number = Column(Integer, autoincrement=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))

class LineItem(Base):
    __tablename__ = 'line_items'
    line_items_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    cookie_id = Column(Integer, ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer)
    extended_cost = Column(Numeric(12, 2))
