from fastapi import APIRouter

router = APIRouter(prefix="/bands")


@router.get("/")
def read_bands():
    pass
