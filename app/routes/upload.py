from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
import os
from app.core.config import settings
from app.utils.file_merge import merge_file_chunks

router = APIRouter()
upload_dir = settings.UPLOAD_DIR
@router.post("/upload_chunk")
async def upload_chunk(file: UploadFile, chunk_index: int = Form(...), filename: str = Form(...), total_chunks: int = Form(...)):
    temp_dir = os.path.join(upload_dir, filename)
    os.makedirs(temp_dir, exist_ok=True)
    chunk_path = os.path.join(temp_dir, f"{chunk_index}.part")
    with open(chunk_path, "wb") as f:
        f.write(await file.read())
    return {"message": f"分片上传 {chunk_index} 成功."}


@router.post("/merge_chunks")
def merge_chunks(filename: str = Form(...), total_chunks: int = Form(...)):
    try:
        result_file_name = merge_file_chunks(filename, total_chunks, upload_dir)
        return {"message": "上传成功", "path": result_file_name}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
