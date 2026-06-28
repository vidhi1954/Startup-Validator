from db import engine
from sqlalchemy import inspect, text

# Check if 'name' column exists in users table
inspector = inspect(engine)
columns = [col['name'] for col in inspector.get_columns('users')]

with engine.begin() as conn:
    # Add 'name' column if it doesn't exist
    if 'name' not in columns:
        conn.execute(text('''
            ALTER TABLE users 
            ADD COLUMN name VARCHAR NOT NULL DEFAULT 'Unknown'
        '''))
        print("✓ Added 'name' column to users table")
    else:
        print("✓ 'name' column already exists")

print("Migration completed - data preserved!")