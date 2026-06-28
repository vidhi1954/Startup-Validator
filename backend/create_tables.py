from database.db import engine
from database.models import Base

# Drop all existing tables first
Base.metadata.drop_all(bind=engine)

# Create all tables fresh
Base.metadata.create_all(bind=engine)

print("Tables created successfully")