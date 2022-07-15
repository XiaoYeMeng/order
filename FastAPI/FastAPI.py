from fastapi import FastAPI
import math
import openpyxl

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


@app.post('/data')
async def data(name: str, mail: str, m_tel: int, tel: int, address: str):
    workbook = openpyxl.Workbook()
    sheet = workbook.worksheets[0]
    sheet.title = '會員資料'
    sheet['A1'] = '姓名'
    sheet['A2'] = name
    sheet['B1'] = '信箱'
    sheet['B2'] = mail
    sheet['C1'] = '手機'
    sheet['C2'] = m_tel
    sheet['D1'] = '電話'
    sheet['D2'] = tel
    sheet['E1'] = '地址'
    sheet['E2'] = address
    workbook.save('會員資料.xlsx')
