from fastapi import APIRouter,Depends
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.other_models import DevelopersModel

from core.deps import get_session 

router = APIRouter()

@router.get('/developers',summary='Retorna todos os gêneros de jogos')
async def get_developers(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DevelopersModel)
        result = await session.execute(query)
        developers : List[DevelopersModel] = result.scalars().all()
        return developers