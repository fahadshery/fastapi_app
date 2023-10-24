from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api.routers.users import router
from api.routers.sections import router_s
from api.routers.courses import router_c

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

app.include_router(router)
app.include_router(router_s)
app.include_router(router_c)


@app.get("/")
async def root():
    return {"message": "Hello world"}
