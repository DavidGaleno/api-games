from fastapi import APIRouter,Path,status,HTTPException,Response,Depends
from typing import List
import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.game_model import GameModel
from schemas.game_schema import GameSchema
from core.deps import get_session 
from sqlalchemy.orm import joinedload
from models.other_models import GenreModel,FranchiseModel,DevelopersModel,PublishersModel

router = APIRouter()

@router.get("/games",summary='Retorna uma lista de games')
async def get_games(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GameModel).options(joinedload(GameModel.genre)).options(joinedload(GameModel.developers)).options(joinedload(GameModel.publisher)).options(joinedload(GameModel.franchise))
        result = await session.execute(query)
        game : List[GameModel] = result.scalars().all()
        return game

@router.get("/games/{id}",summary='Retorna um jogo específico',status_code=status.HTTP_200_OK)
async def get_game(id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0),db: AsyncSession = Depends(get_session)):
   async with db as session:
       query = select(GameModel).filter(id == GameModel.id).options(joinedload(GameModel.genre)).options(joinedload(GameModel.developers)).options(joinedload(GameModel.publisher)).options(joinedload(GameModel.franchise))
       result = await session.execute(query)
       game : GameModel = result.scalar_one_or_none()
       if game:
        return game
       else:
           raise HTTPException(detail='Jogo não encontrado',status_code=status.HTTP_404_NOT_FOUND)
   
@router.post("/games", summary="Cadastra um novo jogo", status_code=status.HTTP_201_CREATED)
async def add_game(game: GameSchema,db: AsyncSession = Depends(get_session)):
    
    genre = await get_genre(db=db,game=game)
    franchise = await get_franchise(db=db,game=game)
    developer = await get_developer(db=db,game=game)
    publisher = await get_publisher(db=db,game=game)

    new_game = GameModel(name=game.name,developer_id=developer.id,publisher_id=publisher.id,franchise_id=franchise.id,genre_id=genre.id,release_date=datetime.date(2000,2,2))

    db.add(new_game)
    await db.commit()
    return new_game
    

@router.put("/games/{id}",status_code=status.HTTP_202_ACCEPTED)
async def update_game(game: GameSchema,id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0),db:AsyncSession = Depends(get_session)):
    async with db as session:
        genre = await get_genre(db=db,game=game)    
        franchise = await get_franchise(db=db,game=game)
        developer = await get_developer(db=db,game=game)
        publisher = await get_publisher(db=db,game=game)
        
        query = select(GameModel).filter(GameModel.id == id)
        result = await session.execute(query)
        game_to_update: GameModel = result.scalar_one_or_none()
        if(game_to_update):
            game_to_update.name = game.name
            game_to_update.developers_id = developer.id
            game_to_update.franchise_id = franchise.id
            game_to_update.genre_id = genre.id
            game_to_update.publisher_id = publisher.id
            game_to_update.release_date = game.release_date
            await session.commit()
            return game_to_update
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
        



async def get_genre(db: AsyncSession, game: GameSchema):
    async with db as session:
        query = select(GenreModel).filter(game.genre == GenreModel.name)
        result = await session.execute(query)
        genre = result.scalar_one_or_none()
        return genre

async def get_franchise(db: AsyncSession, game: GameSchema):
    async with db as session:
        query = select(FranchiseModel).filter(game.franchise == FranchiseModel.name)
        result = await session.execute(query)
        franchise = result.scalar_one_or_none()
        return franchise

async def get_developer(db: AsyncSession, game: GameSchema):
    async with db as session:
        query = select(DevelopersModel).filter(game.developer == DevelopersModel.name)
        result = await session.execute(query)
        developer = result.scalar_one_or_none()
        return developer

async def get_publisher(db: AsyncSession, game: GameSchema):
    async with db as session:
        query = select(PublishersModel).filter(game.publisher == PublishersModel.name)
        result = await session.execute(query)
        publisher = result.scalar_one_or_none()
        return publisher