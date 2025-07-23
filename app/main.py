from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import upload, convert
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

os.makedirs("uploads", exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(upload.router,prefix="/api/upload")
app.include_router(convert.router,prefix="/api/convert")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
