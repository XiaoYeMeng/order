import tkinter as tk

# 驗證是否為數字
def Only_Number(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False

def T():
    ans = (float(entry1.get()) + float(entry2.get())) * float(entry3.get()) / 2
    label4 = tk.Label(window, text=ans, bg='blue', fg='#263238', font=('微軟正黑體', 69))
    label4.grid(column=0, row=30)


# GUI
window = tk.Tk()
# GUI標題
window.title('梯形面積')
# GUI解析度
window.geometry('1024x768')

# 驗證輸入欄位是否為數字
vcmd = (window.register(Only_Number), '%P')

# 上底標籤
label1 = tk.Label(window, text='top', bg='yellow', fg='#263238', font=('微軟正黑體', 69))
# 上底座標
label1.grid(column=0, row=0)
# 上底輸入欄
entry1 = tk.Entry(window, validatecommand=vcmd, validate='key', bg='yellow', font=('微軟正黑體', 69))
# 上底輸入欄座標
entry1.grid(column=10, row=0)

# 下底標籤
label2 = tk.Label(window, text='bot', bg='red', fg='#263238', font=('微軟正黑體', 69))
# 下底座標
label2.grid(column=0, row=10)
# 輸入欄標籤
entry2 = tk.Entry(window, validatecommand=vcmd, validate='key', bg='red', font=('微軟正黑體', 69))
# 輸入欄座標
entry2.grid(column=10, row=10)


# 高標籤
label3 = tk.Label(window, text='high', bg='blue', fg='#263238', font=('微軟正黑體', 69))
# 高座標
label3.grid(column=0, row=20)
# 高輸入欄
entry3 = tk.Entry(window, validatecommand=vcmd, validate='key', bg='blue', font=('微軟正黑體', 69))
# 高輸入欄座標
entry3.grid(column=10, row=20)


# button
bt1 = tk.Button(window, text='ans', bg='orange', fg='#263238', font=('微軟正黑體', 69), command=T)
# button座標
bt1.grid(column=10, row=30)


window.mainloop()
