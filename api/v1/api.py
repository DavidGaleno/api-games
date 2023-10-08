from fastapi import FastAPI,APIRouter
from api.v1.routes import games_router,genre_router

api_router = APIRouter()
api_router.include_router(games_router.router,tags=['games'])
api_router.include_router(genre_router.router,tags=['genres'])

