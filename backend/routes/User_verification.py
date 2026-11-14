from database.db import SessionLocal
from database.models import User
from fastapi import Depends, HTTPException, APIRouter
from models.auth_req import SignupRequest, LoginRequest
from services.auth_services import get_current_user,verify_password,create_access_token,hash_password

router = APIRouter() # lets us group related APIs together

@router.post("/signup")
def signup(request: SignupRequest):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    result = create_user(
        name=request.name,
        email=request.email,
        password=request.password
    )

    db.add(result)
    db.commit()
    db.refresh(result)  # Refresh the user instance to get the generated ID 
    db.close()

    return result

@router.post("/login")
def login(request: LoginRequest):
    db = SessionLocal()

    user = db.query(User).filter(User.email == request.email).first()
    db.close()

    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
    
