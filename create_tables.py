from core.configs import settings
from core.database import engine
from sqlalchemy import insert
async def create_tables() -> None:
    from models.game_model import GameModel
    from models.other_models import GenreModel,FranchiseModel,DevelopersModel,PublishersModel


    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBASEMODEL.metadata.drop_all)
        await conn.run_sync(settings.DBBASEMODEL.metadata.create_all)
    
    async with engine.connect() as conn:
        genres = [{"id" : 1, "name" : 'horror'},{"id": 2, "name": 'action/adventure'},{"id":3,"name":"action"},{"id":4,"name":"hack and slash"},{"id":5,"name":"fps"}]
        query = insert(GenreModel)
        await conn.execute(query.values(genres))
        await conn.commit()

        developers = [{"id" : 1, "name" : 'capcom'},{"id": 2, "name": 'treyarch'},{"id":3,"name":"from software"},{"id":4,"name":"konami"},{"id":5,"name":"dice"}]
        query = insert(DevelopersModel)
        await conn.execute(query.values(developers))
        await conn.commit()

        franchises = [{"id" : 1, "name" : 'call of duty'},{"id": 2, "name": 'resident evil'},{"id":3,"name":"dark souls"},{"id":4,"name":"battlefield"},{"id":5,"name":"devil may cry"}]
        query = insert(FranchiseModel)
        await conn.execute(query.values(franchises))
        await conn.commit()

        publishers = [{"id" : 1, "name" : 'activison'},{"id": 2, "name": 'eletronic arts'},{"id":3,"name":"capcom"},{"id":4,"name":"konami"},{"id":5,"name":"bandai namco"}]
        query = insert(PublishersModel)
        await conn.execute(query.values(publishers))
        await conn.commit()




if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())