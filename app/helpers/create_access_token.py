# ========== Create Access Token ==========
# import all packages
from datetime import timedelta, datetime
from jose import jwt
from app.config.config import Settings

settings = Settings()


def create_access_token(data: dict, minutes: int = 0) -> str :
	to_encode = data.copy()
	expire = datetime.utcnow() + timedelta(minutes=minutes)
	to_encode.update({
		'exp': expire
	})

	return jwt.encode(to_encode, settings.jwt_access_token_secret_key, algorithm=settings.algorithm)