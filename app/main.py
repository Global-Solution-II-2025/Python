from fastapi import FastAPI
from .routes import router as vocational_router

app = FastAPI(title="Vocational API")

app.include_router(vocational_router)
