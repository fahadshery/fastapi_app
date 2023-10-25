from fastapi import FastAPI
from api.routers.users import router
from api.routers.sections import router_s
from api.routers.courses import router_c
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

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
