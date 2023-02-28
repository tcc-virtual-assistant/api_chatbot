from fastapi import APIRouter
from models.question import Question

router = APIRouter()

@router.post("/")
async def add_question(question: Question):
    await question.save()
    return question

@router.get("/")
async def list_question():
    return await Question.objects.all()