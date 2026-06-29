"""
  @Author:lining-lo
  @Time:2026/6/29
  @Desc:fastapi测试
"""

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# 创建FastAPI对象
app = FastAPI()


@app.get("/")
async def request_method01():
    return {"message2222": "hello fastapi"}


@app.get("/items/main")
async def request_method02():
    return {"main": "main"}


@app.get("/items/{item_id}")
async def request_method02(item_id: int, param: str = None):
    return {"item_id": item_id, "param": param}


class User(BaseModel):
    username: str = None
    password: str = None


@app.post("/user")
async def request_method03(user: User):
    return {"user": user}


if __name__ == '__main__':
    uvicorn.run(
        app="fastapi_test:app",
        host="127.0.0.1",
        port=8000,
        reload=True  # 代码修改后自动重启
    )
