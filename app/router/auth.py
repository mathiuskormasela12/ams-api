# ========== Auth Routes ==========
# import all packages
from datetime import timedelta
from fastapi import APIRouter
from jose import JWTError
from app.models.db import db
from app.models.user import User, AuthForm
from app.helpers.hashed_password import generate_hash, verify_hash
from app.helpers.create_access_token import create_access_token
from app.config.config import Settings

settings = Settings()

router = APIRouter()

@router.post('/api/v1/auth/register', tags=['Auth'], status_code=200)
async def register(body: User) -> dict :
	try :
		isExists = db.ams.users.find({
			'username': body.username
		})

		if len(list(isExists)) > 0 :
			return {
				'success': False,
				'message': 'The username is already in used'
			}
		else :
			try :
				hashed = generate_hash(body.password)
				body.password = hashed
				try :
					db.ams.users.insert_one(dict(body))

					return {
						'success': True,
						'message': 'Register successfully, the user has been created'
					}
				except Exception as err :
					print(err)
					return {
						'success': False,
						'message': 'Failed to create a new user'
					}
			except :
				return {
					'success': False,
					'message': 'Failed to generate hash password'
				}
	except :
		return {
			'success': False,
			'message': 'Failed to get a user'
		}

@router.post('/api/v1/auth/login', tags=['Auth'], status_code=200)
async def login(body: AuthForm) -> dict :
	try :
		isExists = list(db.ams.users.find({
			'username': body.username
		})
		)

		if len(isExists) < 1 or verify_hash(body.password, isExists[0]['password']) == False :
			return {
				'success': False,
				'message': 'Username or password is wrong'
			}

		try :
			access_token: str = create_access_token({
				'id': str(isExists[0]['_id'])
			}, minutes=int(settings.jwt_access_token_expires_in))
			return {
				'success': True,
				'message': 'Login Successfully',
				'results': {
					'access_token': access_token
				}
			}
		except JWTError as err :
			print(err)
			return {
				'success': False,
				'message': 'Failed to create an access token'
			}
	except Exception as err:
		print(err)
		return {
			'success': False,
			'message': 'Failed to verify a user'
		}