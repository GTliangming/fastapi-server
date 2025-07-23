# app/core/config.py

import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
    CONVERTED_DIR = os.path.join(BASE_DIR, "converted")

    def __init__(self):
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)
        os.makedirs(self.CONVERTED_DIR, exist_ok=True)


settings = Settings()
