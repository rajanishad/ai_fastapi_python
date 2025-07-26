from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="FastAPI Starter")
app.include_router(router)
