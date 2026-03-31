from fastapi import FastAPI
import fetch_api

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/war_state")
async def get_war_sate():
    x, y = await fetch_api.get_war_state()
    return {"war_state_raw": x, "war_state_json" : y}