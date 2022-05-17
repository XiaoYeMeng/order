import time
import tkinter as tk

# 設定視窗初始化

window = tk.Tk()
window.title('window')
window.geometry('1024x768')
y = 5
time_1 = tk.Label(window, text=y, fg='black', font=('arial', 20))
time_1.pack()


def time_event():
    if time_1['text'] <= 0:
        time_1['text'] = '結束了'
    else:
        x = time_1['text']
        time_1['text'] = x - 1

    window.after(1000, time_event)  # again forever


bt1 = tk.Button(window, text='運算結果', font=('arial', 20), command=time_event)
bt1.pack()

window.mainloop()