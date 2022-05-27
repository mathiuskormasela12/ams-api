# ========== Auth Routes ==========
# import all packages
from fastapi import APIRouter
from app.models.db import db
from app.models.user import User
from app.helpers.hashed_password import generate_hash

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
