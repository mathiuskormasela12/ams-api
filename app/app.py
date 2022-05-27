# ========== App ==========
# import all packages
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.router.auth import router as authRouter

app = FastAPI()

clients = (
	'http://localhost:3000'
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=clients,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="uploads"), name="static")

app.include_router(authRouter)

