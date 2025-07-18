# app/services/tool_service.py
from app.models.tool import ToolRequest, ToolResponse

def process_tool(req: ToolRequest) -> ToolResponse:
    # 你可以在这里调用复杂的逻辑或工具代码
    return ToolResponse(result=f"你输入的是: {req.input}")
