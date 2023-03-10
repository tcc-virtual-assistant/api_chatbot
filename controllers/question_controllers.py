from fastapi import APIRouter, Response
from models.question import Question
import ormar
from models.requests.avillaAnswer_update import avillaAnswerUpdate

router = APIRouter()

@router.post("/")
async def add_question(question: Question):
    await question.save()
    return question

@router.get("/")
async def list_question():
    return await Question.objects.all()

@router.get('/{question_id}')
async def questions_id(question_id: int, response: Response):   
    try: 
        question = await Question.objects.get(id = question_id)
        return question
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'mensagem':'id nao encontrado'}
    
@router.delete('/{question_id}')
async def delete_question(question_id: int, response: Response):
    try:
        question = await Question.objects.get(id = question_id)
        return await question.delete()
    except:
        response.status_code = 404
        return {'mensagem':'id nao encontrado'}

@router.patch('/{question_id}')
async def path_question(avilla_update: avillaAnswerUpdate, question_id: int, response: Response):
    try:
        answer_atualizada = await Question.objects.get(id = question_id)
        answer_propriedades = avilla_update.dict(exclude_unset=True)
        await answer_atualizada.update(**answer_propriedades)
        return answer_atualizada
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'mensagem' : 'Entidade não encontrada'}