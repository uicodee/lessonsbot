from aiogram import Router

from .category import router as category_router
from .lesson import router as lesson_router

router = Router()
router.include_router(category_router)
router.include_router(lesson_router)
