from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rotas import router
import uvicorn

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_root():
    return{"mensagem":"waiting for questions.."}

app.include_router(router, prefix="")