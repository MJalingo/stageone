from fastapi import FastAPI
# from typing import operation_typetional
from pydantic import BaseModel


class Item(BaseModel):
    operation_type: str
    x: int
    y: int

app = FastAPI()

@app.get("/")
def index():
    return  { "slackUsername": "mohammed jalingo nuruddeen", "backend": True, "age": 60, "bio":"python backend developer" }

@app.post('/items/')
async def do_operation(res: Item):
    res_dict = {}
    if res.operation_type == "addition":
        result = res.x + res.y
        res_dict.update({"slackUsername": "mohammed jalingo nuruddeen","result": result,'operation_type':res.operation_type})
    elif res.operation_type == "subtraction":
        result = res.x - res.y
        res_dict.update({"slackUsername": "mohammed jalingo nuruddeen","result": result,'operation_type':res.operation_type})
    elif res.operation_type == "multiplication":
        result = res.x * res.y
        res_dict.update({"slackUsername": "mohammed jalingo nuruddeen","result": result,'operation_type':res.operation_type})
    return res_dict
