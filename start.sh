#!/bin/bash

# 启动 FastAPI 应用（多进程方式）
uvicorn app.main:app --host 0.0.0.0  --port 8088 --timeout 300 --workers 1 --log-level info