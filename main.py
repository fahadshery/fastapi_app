from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fahad's Test Fast API App",
    description="Following the official tutorial and the YouTube Tutorial at: https://www.youtube.com/watch?v=gQTRsZpR7Gw",
    summary="Exploring and learning about FastAPI",
    version="0.0.1",
    contact={
        "name": "Fahad Usman",
        "url": "https://fahadusman.com/contact/",
        "email": "fahadshery@yahoo.com",
    },
    license_info={
        "name": "MIT",
    },
)

in_memory_users_list = []


class User(BaseModel):
    name: str
    email: str
    bio: Optional[str]
    is_active: bool


@app.get("/")
async def root():
    return {"message": "Hello World! This is Fahad"}


@app.get("/user", response_model=List[User])
async def get_user():
    return in_memory_users_list


@app.get("/user/{id}")
async def get_user(
    id: int = Path(..., description="Enter User ID", ge=1),
    test_var: str = Query(
        None, max_length=3, description="Test var, only enter max 3 letters"
    ),
):
    return {"user_id": in_memory_users_list[id], "test_var": test_var}


@app.post("/user")
async def create_user(user: User):
    in_memory_users_list.append(user)
    return {"message": "Your user has been added"}
