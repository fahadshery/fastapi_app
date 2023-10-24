import fastapi

router_s = fastapi.APIRouter()


@router_s.get("/sections/{id}")
async def read_sections():
    return {"courses": []}


@router_s.get("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router_s.get("/content-blocks/{id}")
async def read_content_block():
    return {"courses": []}
