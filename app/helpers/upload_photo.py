# ========== Upload Photo ==========
# import all packages
import datetime
import shutil

def upload_photo(file) -> str :
	file_name = file.filename.split('.')
	ext = file_name[int(len(file_name)) - 1].lower()
	file_name = file_name[0].lower()
	file_name += '-'
	file_name += str(datetime.datetime.now())
	file_name += '.'
	file_name += ext

	with open(f'uploads/{file_name}', 'wb') as buffer :
		shutil.copyfileobj(file.file, buffer)
	
	return file_name
	
