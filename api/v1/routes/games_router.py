from fastapi import APIRouter,Path,status,HTTPException,Response,Depends
from typing import List
import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.game_model import GameModel
from schemas.game_schema import GameSchema
from core.deps import get_session 

from models.game_model import GameModel

router = APIRouter()

@router.get("/games",summary='Retorna uma lista de games')
async def get_games(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GameModel)
        result = await session.execute(query)
        game : List[GameModel] = result.scalars().all()
        return game

@router.get("/games/{id}",summary='Retorna um jogo específico',status_code=status.HTTP_200_OK)
async def get_game(id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0),db: AsyncSession = Depends(get_session)):
   async with db as session:
       query = select(GameModel).filter(id == GameModel.id)
       result = await session.execute(query)
       game : GameModel = result.scalar_one_or_none()
       if game:
        return game
       else:
           raise HTTPException(detail='Jogo não encontrado',status_code=status.HTTP_404_NOT_FOUND)
   
@router.post("/games", summary="Cadastra um novo jogo", status_code=status.HTTP_201_CREATED)
async def add_game(game: GameSchema,db: AsyncSession = Depends(get_session)):
    new_game = GameModel(name=game.name,developer=game.developer,publisher=game.publisher,franchise=game.franchise,genre=game.genre,release_date=datetime.date(2000,2,2))

    db.add(new_game)
    await db.commit()
    return new_game
    

@router.put("/games/{id}",response_model=GameSchema,status_code=status.HTTP_202_ACCEPTED)
async def update_game(game: GameSchema,id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0),db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GameModel).filter(GameModel.id == id)
        result = await session.execute(query)
        game_to_update: GameModel = result.scalar_one_or_none()

        if(game_to_update):
            game_to_update.name = game.name
            game_to_update.developer = game.developer
            game_to_update.franchise = game.franchise
            game_to_update.genre = game.genre
            game_to_update.release_date = game.release_date
            await session.commit()
            return game
        else:
            raise HTTPException(detail='Jogo não encontrado',status_code=status.HTTP_404_NOT_FOUND)

    
@router.delete("/games/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0),db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GameModel).filter(GameModel.id == id)
        result = await session.execute(query)
        game_to_delete = result.scalar_one_or_none()

        if(game_to_delete):
            await session.delete(game_to_delete)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Jogo não encontrado',status_code=status.HTTP_404_NOT_FOUND)
    