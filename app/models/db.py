# ========== Database ==========
# import all packages
from pymongo import MongoClient
from app.config.config import Settings

settings = Settings()

db = MongoClient(settings.db_uri)