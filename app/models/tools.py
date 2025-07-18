# app/models/tool.py
from pydantic import BaseModel

class ToolRequest(BaseModel):
    input: str

class ToolResponse(BaseModel):
    result: str
