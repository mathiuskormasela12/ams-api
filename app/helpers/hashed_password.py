# ========== Hashed Password ==========
# import all packages
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def generate_hash(password: str) -> str :
	return pwd_context.hash(password)

def verify_hash(password: str, hash: str) -> bool :
	return pwd_context.verify(password, hash)