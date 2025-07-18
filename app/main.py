# app/main.py
from fastapi import FastAPI
from app.api.v1 import tools

app = FastAPI()

# 注册路由
app.include_router(tools.router, prefix="/api/v1/tools")
