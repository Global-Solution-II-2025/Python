from fastapi import FastAPI
from app.config import settings, setup_cors
from app.database import init_db
from app.routes import users, answers, profile, career

def create_app():
    app = FastAPI(title="Career AI API", version="1.0")
    setup_cors(app)
    init_db()
    app.include_router(users.router, prefix="/users", tags=["Users"])
    app.include_router(answers.router, prefix="/responses", tags=["Chatbot"])
    app.include_router(profile.router, prefix="/profile", tags=["Profiles"])
    app.include_router(career.router, prefix="/career", tags=["Career"])
    return app

app = create_app()
