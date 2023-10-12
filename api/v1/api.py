from fastapi import FastAPI,APIRouter
from api.v1.routes import games_router,genre_router,franchises_router,developers_router,publishers_router

api_router = APIRouter()
api_router.include_router(games_router.router,tags=['games'])
api_router.include_router(genre_router.router,tags=['genres'])
api_router.include_router(franchises_router.router,tags=['franchises'])
api_router.include_router(developers_router.router,tags=['developers'])
api_router.include_router(publishers_router.router,tags=['publishers'])

