from fastapi import APIRouter, HTTPException

from database.db import SessionLocal
from database.models import User
from models.auth_req import LoginRequest, SignupRequest
from services.auth_services import create_access_token, verify_password
from services.user_verification_service import create_user

router = APIRouter()


@router.post("/signup")
def signup(request: SignupRequest):
    try:
        result = create_user(
            name=request.name,
            email=request.email,
            password=request.password,
        )

        if not result.get("success"):
            raise HTTPException(status_code=400, detail=result.get("message"))

        return {
            "success": True,
            "message": result.get("message"),
            "user_id": result.get("user_id"),
        }
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Signup failed: {str(exc)}") from exc


@router.post("/login")
def login(request: LoginRequest):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == request.email).first()
        if not user or not verify_password(request.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_access_token(int(user.id))
        return {"access_token": token, "token_type": "bearer"}
    finally:
        db.close()

