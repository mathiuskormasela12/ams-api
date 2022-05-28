# ========== App Config ==========
# import all packages
from pydantic import BaseSettings

class Settings(BaseSettings):
	port: int
	host: str
	env: str
	db_uri: str
	jwt_access_token_secret_key: str
	jwt_refresh_token_secret_key: str
	jwt_access_token_expires_in: str
	jwt_refresh_token_expires_in: str
	algorithm: str

	class Config:
		env_file = ".env"
