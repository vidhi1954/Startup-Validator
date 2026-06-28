from database.db import SessionLocal
from database.models import User

db = SessionLocal()

user = User(
    id=1,
    name="Test User",
    email="test@gmail.com",
    password_hash="abc123"
)

db.add(user)

db.commit()

print("User inserted")