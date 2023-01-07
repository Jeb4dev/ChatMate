from fastapi import APIRouter

from .endpoints.users import router as users_router

router = APIRouter()
router.include_router(users_router, prefix="/users", tags=["users"])
