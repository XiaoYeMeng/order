from fastapi import FastAPI
import math

app = FastAPI()


@app.post('/circle')
async def circle(radius: float):
    pi = math.pi
    answer = radius * radius * pi
    open('test_ans.txt', 'a+')
    return answer


@app.post('/rectangle')
async def quadrilateral(long: float, width: float):
    answer = long * width
    return answer


@app.post('/triangle')
async def triangle(bot: float, height: float):
    answer = bot * height / 2
    return answer


