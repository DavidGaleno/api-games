from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def game_test():
    return {"name": "Starfie ld","publisher":"Microsoft","developer":"Bethesda Studios", "release_date":"2023-08-06","plataforms":["Steam","Xbox"]}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app",host="localho st", port=8000,log_level="info",reload=True)