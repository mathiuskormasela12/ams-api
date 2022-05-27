# ========== Main ==========
# import all packages
import uvicorn
from app.config.config import appConfig

if __name__ == '__main__' :
	reload = False

	if appConfig['ENV'] == 'dev' :
		reload = True
		
	uvicorn.run('app.app:app', host=appConfig['HOST'], port=appConfig['PORT'], reload=reload)