import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import openpyxl
import pygame


def en_1():
    if et_1.get() <= '0' or et_2.get() <= '0' or et_3.get() <= '0' :
        tk.messagebox.showerror('error', 'Enter a value.')
    else:
        count = '(' + et_1.get() + '+' + et_2.get() + ')' + ' * ' + et_3.get() + ' / 2' + ' = '
        answer = str((float(et_1.get()) + float(et_2.get())) * float(et_3.get()) / 2)
        lb_5['text'] = count + answer
        lb_6['image'] = img_1
        # 建立一個新的工作簿
        workbook = openpyxl.Workbook()
        # 取得第一個工作表
        sheet = workbook.worksheets[0]
        # 設定 sheet 工作表 A1 儲存格內容
        sheet['A1'] = 'top'
        sheet['A2'] = 'bot'
        sheet['A3'] = 'height'
        sheet['A4'] = 'ans'
        sheet['B1'] = (et_1.get())
        sheet['B2'] = (et_2.get())
        sheet['B3'] = (et_3.get())
        sheet['B4'] = count + answer
        # 儲存檔案
        workbook.save('homeWork.xlsx')


def en_2():
    lb_5['text'] = '(top+bot) * height / 2'
    lb_6['image'] = img_2
    et_1.delete(0, 'end')
    et_2.delete(0, 'end')
    et_3.delete(0, 'end')


"""
GUI
"""
window = tk.Tk()
window.title('HomeWork')
window.geometry('1024x960')

"""
Image
"""
# 圖片路徑
img_1 = ImageTk.PhotoImage(Image.open('./image/ITACHI_1_960x540.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('./image/clear.jpg'))

"""
Label
"""
# 上底標籤
lb_1 = tk.Label(window, width=5, text='top', bg='red', font=('微軟正黑體', 36))
lb_1.grid(column=0, row=0)
# 下底標籤
lb_2 = tk.Label(window, width=5, text='bot', bg='orange', font=('微軟正黑體', 36))
lb_2.grid(column=0, row=1)
# 高標籤
lb_3 = tk.Label(window, width=5, text='height', bg='yellow', font=('微軟正黑體', 36))
lb_3.grid(column=0, row=2)
# 答案標籤
lb_4 = tk.Label(window, width=5, text='ans', bg='green', font=('微軟正黑體', 36))
lb_4.grid(column=0, row=3)
# 公式標籤
lb_5 = tk.Label(window, text='(top+bot) * height / 2', font=('微軟正黑體', 36))
lb_5.place(x=160, y=200)
# 圖片標籤
lb_6 = tk.Label(window, width=960, height=540)
lb_6.place(x=0, y=390)

"""
Entry
"""
# 上底輸入欄
et_1 = tk.Entry(window, bg='red', font=('微軟正黑體', 36))
et_1.grid(column=1, row=0)
# 下底輸入欄
et_2 = tk.Entry(window, bg='orange', font=('微軟正黑體', 36))
et_2.grid(column=1, row=1)
# 高輸入欄
et_3 = tk.Entry(window, bg='yellow', font=('微軟正黑體', 36))
et_3.grid(column=1, row=2)
"""
Button
"""
# 計算按鈕
bt_1 = tk.Button(window, text='count', bg='blue', font=('微軟正黑體', 36), command=en_1)
bt_1.place(x=180, y=270)
# 重置按鈕
bt_2 = tk.Button(window, text='reset', bg='blue', font=('微軟正黑體', 36), command=en_2)
bt_2.place(x=420, y=270)

'''
播放MP3
'''
pygame.mixer.init()
pygame.mixer.music.load('./mp3/NextToYou.mp3')
pygame.mixer.music.play(-1)


window.mainloop()
