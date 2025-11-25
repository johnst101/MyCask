# Quick test script (save as test_db.py in backend/)
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://mycask:mycask123@localhost:5432/mycask")

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("✅ Database connected!")
        print(f"PostgreSQL version: {result.fetchone()[0]}")
except Exception as e:
    print(f"❌ Connection failed: {e}")