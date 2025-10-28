from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def greet():
    return {"Hello": "Welcome to the world of Tea!!!"}

class Tea(BaseModel):
    id: int
    name: str
    origin: str


teas: List[Tea] = []

@app.get("/teas")
def tea():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    return teas.append(tea)

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
        else:
            return {"error": "Tea not found :("}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea_id == tea.id:
            return teas.pop[index]
    return {"error": "Tea not found :("}
    