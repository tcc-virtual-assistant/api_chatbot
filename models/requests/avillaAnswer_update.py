from typing import List, Optional
from pydantic import BaseModel

class avillaAnswerUpdate(BaseModel):
    userQuestion: Optional[str] = None
    avillaAnswer: Optional[str] = None