from fastapi import APIRouter,Depends
from typing import List

from schemas.franchise_schema import FranchiseSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.other_models import FranchiseModel

from core.deps import get_session 

router = APIRouter()

@router.get('/franchises',summary='Retorna todos os gêneros de jogos')
async def get_franchises(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FranchiseModel)
        result = await session.execute(query)
        franchises : List[FranchiseModel] = result.scalars().all()
        return franchises