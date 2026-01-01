import uvicorn
from fastapi import FastAPI

from app.routers import router

app = FastAPI(title="FastAPI Multi Tenancy")
app.include_router(router)

if __name__ == "__main__":
    app_name: str = "main:app"
    uvicorn.run(app_name, host="0.0.0.0", port=80, reload=True)
