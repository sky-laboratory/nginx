from fastapi import FastAPI
from typing import Union
from datetime import datetime

app = FastAPI()


@app.get("/user")
def users():
    strart_time = datetime.now()
    return {"test": f"현재 시각 : {strart_time} user API 호출되었습니다"}


@app.get("/items")
def read_item():
    strart_time = datetime.now()
    return {"test": f"현재 시각 : {strart_time} items API 호출되었습니다"}

