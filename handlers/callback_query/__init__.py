from aiogram import Router

from .back import router as back_router
from .category import router as category_router
from .lesson import router as lesson_router

router = Router()
router.include_router(back_router)
router.include_router(category_router)
router.include_router(lesson_router)
