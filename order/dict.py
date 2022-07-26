import pandas as pd

menu_a = pd.read_excel('menu.xlsx', sheet_name='menu', usecols='A')
menu_b = pd.read_excel('menu.xlsx', sheet_name='menu', usecols='B')
menu_c = pd.read_excel('menu.xlsx', sheet_name='menu', usecols='C')
menu_d = pd.read_excel('menu.xlsx', sheet_name='menu', usecols='D')

dict_menu = {'產品名稱': menu_a, '產品圖片': menu_b, '產品資訊': menu_c, '產品價格': menu_d}
