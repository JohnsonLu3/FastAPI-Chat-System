from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthService:
    def __init__(self, db):
        self.db = db

    def fake_hash_password(self, password: str):
        return "fakehashed" + password

    def get_user(self, username: str):
        if username in self.db:
            user_dict = self.db[username]
            return UserInDB(**user_dict)
        return None

    def fake_decode_token(self, token):
        # This doesn't provide any security at all
        # Check the next version
        user = self.get_user(token)
        return user

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        user = self.fake_decode_token(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user

    async def get_current_active_user(self, current_user: User = Depends(get_current_user)):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user

    async def login(self, form_data: OAuth2PasswordRequestForm = Depends()):
        user_dict = self.db.get(form_data.username)
        if not user_dict:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        user = UserInDB(**user_dict)
        hashed_password = self.fake_hash_password(form_data.password)
        if hashed_password != user.hashed_password:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        return {"access_token": user.username, "token_type": "bearer"}
