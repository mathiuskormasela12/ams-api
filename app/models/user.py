# ========== User Model ==========
# import all packages
from pydantic import BaseModel

class User(BaseModel) :
	first_name: str
	last_name: str
	username: str
	photo: str = 'nophoto.png'
	password: str
