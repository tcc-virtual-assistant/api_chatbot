from fastapi import FastAPI
from router import Router

app = FastAPI()

@app.get("/")
def get_root():
    return{"mensagem":"waiting for questions.."}

app.include_router(router, prefix="")