import ormar
from config import database, metadata

class Question(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'questions'

    id: int = ormar.Integer(primary_key=True)
    userQuestion: str = ormar.String(max_length = 200)
    avillaAnswer: str = ormar.String(max_length=200)