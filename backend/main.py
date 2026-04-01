from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import fetch_api

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/war_state")
async def get_war_sate():
    x = await fetch_api.get_war_state()
    print(x)
    return {"war_state": x}
    