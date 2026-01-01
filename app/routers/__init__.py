from fastapi import APIRouter

from . import api

router = APIRouter(prefix="")
router.include_router(api.router)
