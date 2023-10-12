from fastapi import APIRouter,Depends
from typing import List

from schemas.franchise_schema import FranchiseSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.other_models import PublishersModel

from core.deps import get_session 

router = APIRouter()

@router.get('/publishers',summary='Retorna todos os gêneros de jogos')
async def get_publishers(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PublishersModel)
        result = await session.execute(query)
        publishers : List[PublishersModel] = result.scalars().all()
        return publishers