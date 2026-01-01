from fastapi import APIRouter

from . import bands

router = APIRouter(prefix="/v1")
router.include_router(bands.router)
