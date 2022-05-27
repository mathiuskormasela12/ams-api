# ========== User Schema ==========

def userEntity(item) -> dict :
	return {
		'id': str(item['_id']),
		'first_name': item['first_name'],
		'last_name': item['last_name'],
		'username': item['username'],
		'photo': item['photo'],
		'password': item['password']
	}

def usersEntity(entity) -> list :
	return [userEntity(item) for item in entity]