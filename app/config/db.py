# ========== Database ==========
# import all packages
from pymongo import MongoClient
from app.config.config import appConfig

db = MongoClient(appConfig['DB_URI'])