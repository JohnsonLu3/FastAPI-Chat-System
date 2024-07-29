from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..services.auth import AuthService, User

# Dummy user database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    }
}

auth_service = AuthService(fake_users_db)

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await auth_service.login(form_data)

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(auth_service.get_current_active_user)):
    return current_user