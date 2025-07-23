from fastapi import APIRouter, HTTPException
from app.core.config import settings
import os
import glob
from pydantic import BaseModel
from app.utils.psd_tools import convert_psd_to_format, merge_file_chunks
router = APIRouter()


class ConvertRequest(BaseModel):
    filename: str  # 原始完整文件名，如：xxx.psd
    target_format: str  # jpg, png 等

@router.post("/")
def convert_file(req: ConvertRequest):
    filename = req.filename
    target_format = req.target_format.lower()

    psd_path = os.path.join(settings.UPLOAD_DIR, filename)
    target_path = os.path.join(settings.UPLOAD_DIR, f"{filename}.{target_format}")
    convert_psd_to_format(psd_path, target_path)
    return {
        "success": True,
        "converted_url": f"/{filename}.{target_format}"
    }
