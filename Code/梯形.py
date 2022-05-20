# 計算梯形面積

import tkinter as tk

# 公式
print('計算梯形面積')
top = input('輸入上底')
bot = input('輸入下底')
high = input('輸入高')
ans = (float(top) + float(bot)) * float(high) / 2
print(type(ans))

# GUI
window = tk.Tk()
window.title('梯形面積')
window.geometry('1024x768')
tk.Label(window, text='梯形面積='+str(ans), font=('微軟正黑體', 69)).grid()


# 匯出txt
ans69 = open('梯形面積.txt', 'a+')
print('梯形面積='+str(ans), file=ans69)

window.mainloop()
