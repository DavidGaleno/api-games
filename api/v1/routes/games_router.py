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
        cursos : List[GameModel] = result.scalars().all()
        return cursos

@router.get("/games/{id}",summary='Retorna um jogo específico')
async def get_game(id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0)):
   pass
   
@router.post("/games", summary="Cadastra um novo jogo", status_code=status.HTTP_201_CREATED)
async def add_game(game: GameSchema,db: AsyncSession = Depends(get_session)):
    new_game = GameModel(name=game.name,developer=game.developer,publisher=game.publisher,franchise=game.franchise,genre=game.genre,release_date=datetime.date(2000,2,2))

    db.add(new_game)
    await db.commit()
    return new_game
    

@router.put("/games/{id}")
async def update_game(id: int,game : GameSchema):
    pass
    
@router.delete("/games/{id}")
async def delete_game(id: int):
    pass