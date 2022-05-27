# ========== App Config ==========
# import all packages
from pydantic import BaseSettings

class Settings(BaseSettings):
	port: int
	host: str
	env: str
	db_uri: str

	class Config:
		env_file = ".env"
