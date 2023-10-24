import fastapi

router_c = fastapi.APIRouter()


@router_c.get("/courses/{id}")
async def read_course(id):
    return {"course": []}


@router_c.get("/courses")
async def read_courses():
    return {"course": []}


@router_c.post("/courses")
async def create_course():
    return {"message": "course been added successfully"}


@router_c.patch("/courses/{id}")
async def update_course(id):
    return {"message": "course been updated successfully"}


@router_c.delete("/courses/{id}")
async def delete_course(id):
    return {"message": "course been deleted successfully"}
