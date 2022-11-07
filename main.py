from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    op: str
    x: int
    y: int

app = FastAPI()

@app.get("/")
def index():
    return  { "slackUsername": "mohammed jalingo nuruddeen", "backend": True, "age": 60, "bio":"python backend developer" }

@app.post('/items/')
async def do_operation(res: Item):
    res_dict = {}
    if res.op == "addition":
        result = res.x + res.y
        res_dict.update({"result": result})
    elif res.op == "subtraction":
        result = res.x - res.y
        res_dict.update({"result": result})
    elif res.op == "multiplication":
        result = res.x * res.y
        res_dict.update({"result": result})
    return res_dict
