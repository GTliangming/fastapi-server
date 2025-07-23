import uvicorn

print("Starting FastAPI app...")
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8088, reload=True)
