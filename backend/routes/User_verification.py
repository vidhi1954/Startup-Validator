from models.auth_req import SignupRequest, LoginRequest
from fastapi import APIRouter
from services.user_verification_service import create_user, login_user

router = APIRouter() # lets us group related APIs together

@router.post("/signup")
def signup(request: SignupRequest):
    result = create_user(
        name=request.name,
        email=request.email,
        password=request.password
    )

    return result

@router.post("/login")
def login(request: LoginRequest):
    result = login_user(
        email=request.email,
        password=request.password
    )

    return result
