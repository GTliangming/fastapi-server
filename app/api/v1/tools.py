# app/api/v1/tools.py
from fastapi import APIRouter
from app.models.tool import ToolRequest, ToolResponse
from app.services.tool_service import process_tool

router = APIRouter()

@router.post("/run", response_model=ToolResponse)
def run_tool(req: ToolRequest):
    return process_tool(req)
