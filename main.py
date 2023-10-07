from fastapi import FastAPI
from models.game import Game
import datetime

app = FastAPI()

@app.get("/")
async def game_test():
    game = Game(name='Starfield',developer='Bethesda',franchise='Starfield',genre=['Action','RPG','FPS'],publisher='Microsoft',release_date=datetime.date(2023,9,6))
    return game

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app",host="localhost", port=8000,log_level="info",reload=True)