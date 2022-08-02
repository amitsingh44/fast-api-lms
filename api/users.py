from ctypes.wintypes import INT
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]



@router.get('/', response_model=List[User])
async def get_users():
    return users


@router.post('/users')
async def create_user(user: User):
    users.routerend(user)
    return "Success!"


@router.get("/users/{id}")
async def get_user(id:int):
    return {"id": users[id]}