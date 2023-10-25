from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

in_memory_users_list = []


class User(BaseModel):
    name: str
    email: str
    bio: Optional[str]
    country: str | None = None
    is_active: bool


@router.get("/user", response_model=List[User])
async def get_user():
    return in_memory_users_list


@router.get("/user/{id}")
async def get_user(id: int):
    return {"user_id": in_memory_users_list[id]}


@router.post("/user")
async def create_user(user: User):
    in_memory_users_list.append(user)
    return {"message": "Your user has been added"}
