import os
import shutil

def merge_file_chunks(filename: str, total_chunks: int, upload_dir: str):
    temp_dir = os.path.join(upload_dir, filename)  # 存放分片的目录
    # 这里给合并后的文件加个扩展名，防止和目录重名
    result_file_name = f"{filename}.psd"
    output_path = os.path.join(upload_dir, result_file_name)

    with open(output_path, "wb") as merged:
        for i in range(total_chunks):
            chunk_path = os.path.join(temp_dir, f"{i}.part")
            if not os.path.exists(chunk_path):
                raise FileNotFoundError(f"Missing chunk: {chunk_path}")
            with open(chunk_path, "rb") as chunk_file:
                shutil.copyfileobj(chunk_file, merged)

    shutil.rmtree(temp_dir)  # 合并后删除临时目录
    return result_file_name
