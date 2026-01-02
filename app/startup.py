# startup.py
from db import create_tables

def init_app():
    create_tables()  # runs once at app startup
    print("Tables created (if they didn't exist)")

if __name__ == "__main__":
    init_app()
