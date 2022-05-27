# ========== Main ==========
# import all packages
import uvicorn
from app.config.config import Settings

settings = Settings()

if __name__ == '__main__' :
	reload = False

	if settings.env == 'dev' :
		reload = True
		
	uvicorn.run('app.app:app', host=settings.host, port=settings.port, reload=reload)