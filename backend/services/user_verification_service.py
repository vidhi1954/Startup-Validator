from database.db import SessionLocal
from database.models import User
from services.auth_services import hash_password, verify_password


def create_user(name: str, email: str, password: str):
    db = SessionLocal()

    try:
        existing_user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if existing_user:
            return {
                "success": False,
                "message": "Email already exists",
            }

        user = User(
            name=name,
            email=email,
            password_hash=hash_password(password),
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "success": True,
            "message": "User created successfully",
            "user_id": user.id,
            "user": user,
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
                "message": "User not found",
            }

        if not verify_password(password, user.password_hash):
            return {
                "success": False,
                "message": "Incorrect password",
            }

        return {
            "success": True,
            "message": "Login successful",
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
        }
    finally:
        db.close()