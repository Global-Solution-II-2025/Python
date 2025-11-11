from datetime import datetime, timedelta
import jwt
from app.config import settings

def create_jwt_token(subject: str, expires_minutes: int = None):
    expires_minutes = expires_minutes or settings.JWT_EXPIRATION_MINUTES
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "exp": expire}
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except Exception:
        return None
