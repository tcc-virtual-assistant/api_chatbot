from fastapi import APIRouter
from controllers import question_controllers as question

router = APIRouter()

router.include_router(question.router, prefix='/question')