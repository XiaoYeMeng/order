from fastapi import FastAPI

app = FastAPI()


@app.get('/menu')
async def menu():
    pass