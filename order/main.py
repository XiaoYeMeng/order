from fastapi import FastAPI
import openpyxl

app = FastAPI()


@app.get('/')
async def test():
    workbook = openpyxl.Workbook()
    sheet = workbook.worksheets[0]
    sheet.title = 'Menu'
    sheet['A1'] = '產品名稱'
    sheet['B1'] = '產品圖片'
    sheet['C1'] = '產品資訊'
    sheet['D1'] = '產品價格'
    workbook.save('Menu.xlsx')




