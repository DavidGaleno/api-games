from fastapi import APIRouter,Path,status,HTTPException,Response,Depends
from typing import List

from schemas.genre_schema import GenreSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.other_models import GenreModel

from core.deps import get_session 

router = APIRouter()

@router.get('/genres',summary='Retorna todos os gêneros de jogos')
async def get_genres(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GenreModel)
        result = await session.execute(query)
        genres : List[GenreModel] = result.scalars().all()
        return genres
    
@router.get('/genres/{id}',summary='Retorna um jogo específico')
async def get_genre(id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0,),db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GenreModel).filter(GenreModel.id == id)
        result = await session.execute(query)
        genre = result.scalar_one_or_none()
        if(genre):
            return genre
        else:
            raise HTTPException(detail='Jogo não encontrado',status_code=status.HTTP_404_NOT_FOUND)


@router.put('/genres/{id}',summary='Atualiza um jogo')
async def update_genre(genre:GenreSchema,id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0),db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GenreModel).filter(GenreModel.id == id)
        result = await session.execute(query)
        genre_to_update: GenreModel = result.scalar_one_or_none()
        print(genre.name)
        print(genre_to_update.name)
        if(genre_to_update):
            genre_to_update.name = genre.name
            await session.commit()
            return genre_to_update
        else:
            raise HTTPException(detail='Jogo não encontrado',status_code=status.HTTP_404_NOT_FOUND)

@router.delete('/genres/{id}',summary='Deleta um jogo')
async def delete_genre(id: int = Path(title='id do jogo',description='Deve ser maior que 0',gt=0),db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GenreModel).filter(GenreModel.id == id)
        result = await session.execute(query)
        game_to_delete = result.scalar_one_or_none()
        
        if(game_to_delete):
            await session.delete(game_to_delete)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Jogo não encontrado',status_code=status.HTTP_404_NOT_FOUND)
