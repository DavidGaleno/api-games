from core.configs import settings
from core.database import engine

async def create_tables() -> None:
    from models.game_model import GameModel
    from models.other_models import GenreModel,FranchiseModel,DevelopersModel,PublishersModel


    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBASEMODEL.metadata.drop_all)
        await conn.run_sync(settings.DBBASEMODEL.metadata.create_all)

if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())