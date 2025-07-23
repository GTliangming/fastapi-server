# app/utils/psd_tools.py

import os
import psutil
from PIL import Image
from psd_tools import PSDImage
import gc


def log_resource_usage(tag=""):
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # 转成 MB
    cpu = process.cpu_percent(interval=0.1)  # 注意这个是个瞬时值
    print(f"[{tag}] 内存占用: {mem:.2f} MB | CPU占用: {cpu:.2f}%")

def merge_file_chunks(chunk_paths, output_path):
    with open(output_path, 'wb') as outfile:
        for chunk in chunk_paths:
            with open(chunk, 'rb') as infile:
                outfile.write(infile.read())


def convert_psd_to_format(psd_path, output_path):
    try:
        print(f"开始处理 PSD: {psd_path}")
        log_resource_usage("加载前")

        psd = PSDImage.open(psd_path)

        log_resource_usage("PSD加载后")


        composite = psd.composite()

        log_resource_usage("合并图层后")

        rgb_image = composite.convert("RGB")

        log_resource_usage("convert后")


        rgb_image.save(output_path)

        log_resource_usage("保存图像后")

    except Exception as e:
        raise RuntimeError(f"转换失败: {e}")