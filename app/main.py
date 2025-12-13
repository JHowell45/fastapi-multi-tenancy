import uvicorn
from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    app_name: str = "main:app"
    uvicorn.run(app_name, host="0.0.0.0", port=80, reload=True)
