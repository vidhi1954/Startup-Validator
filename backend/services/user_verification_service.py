from database.db import SessionLocal
from database.models import User


def create_user(name: str, email: str, password: str):

    db = SessionLocal()

    try:
        # Check if email already exists
        existing_user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if existing_user:
            return {
                "success": False,
                "message": "Email already exists"
            }

        # Create user object
        user = User(
            name=name,
            email=email,
            password_hash=password
        )

        db.add(user)
        db.commit()
        db.refresh(user) # now user.id will get value from the updated DB

        return {
            "success": True,
            "message": "User created successfully",
            "user_id": user.id
        }

    finally:
        db.close()


def login_user(email: str, password: str):

    db = SessionLocal()

    try:
        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if user is None:
            return {
                "success": False,
                "message": "User not found"
            }

        if user.password_hash != password:
            return {
                "success": False,
                "message": "Incorrect password"
            }

        return {
            "success": True,
            "message": "Login successful",
            "user_id": user.id,
            "name": user.name,
            "email": user.email
        }

    finally:
        db.close()