from fastapi import FastAPI
from api.v1.api import api_router
from core.configs import settings

app = FastAPI(title='Games Database API',description="This api is used to get data that interests investors, fans and developers. This is a college project of the discipline Advanced Topics of Programming",version='0.0.1',)


app.include_router(api_router,prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app",host="localhost", port=8000,log_level="info",reload=True)