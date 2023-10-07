from fastapi import APIRouter,Path,status,HTTPException,Response
from typing import List
import datetime
from models.game import Game

router = APIRouter()

games : List[Game] = [Game(name='starfield',developer='bethesda',franchise='starfield',genre=['action','rpg','fps'],publisher='microsoft',release_date=datetime.date(2023,9,6)), Game(name='resident_evil_4',developer='capcom',franchise='resident_evil',genre=['action_adventure','3° person shooter','horror'],publisher='capcom',release_date=datetime.date(2005,2,10))]


@router.get("/games",summary='Retorna uma lista de games',response_model=List[Game])
async def get_games():
    return games

@router.get("/games/{id}",summary='Retorna um jogo específico',response_model=Game)
async def get_game(id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0)):
   try:
       game = games[id - 1]
       return game
   except KeyError:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Jogo não encontrado')
   
@router.post("/games")
async def add_game(game: Game):
    if game not in games:
        games.append(game)
        return game
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Jogo já cadastrado')

@router.put("/games/{id}")
async def update_game(id: int,game : Game):
    try:
        index = id - 1
        games[index] = game
        return game
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Jogo não encontrado')
    
@router.delete("/games/{id}")
async def delete_game(id: int):
    try:
        index = id - 1
        games.pop(index)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Jogo não encontrado')