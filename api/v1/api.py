from fastapi import FastAPI,APIRouter
from api.v1.routes import games_router

api_router = APIRouter()
api_router.include_router(games_router.router,tags=['games'])

