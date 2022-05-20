import tkinter as tk
from tkinter import messagebox
import openpyxl


def debug():
    try:
        float(et_top.get())
        float(et_bot.get())
        float(et_height.get())
    except ValueError:
        messagebox.showerror('error', 'Enter a value.')
    else:
        count = str('(' + et_top.get() + '+' + et_bot.get() + ')' + ' * ' + et_height.get() + ' / ' + ' 2 ' + ' = ')
        ans = str((float(et_top.get()) + float(et_bot.get())) * float(et_height.get()) / 2)
        lb_answer['text'] = count + ans
 #       workbook = openpyxl.Workbook()


def reset():
    et_top.delete(0, 'end')
    et_bot.delete(0, 'end')
    et_height.delete(0, 'end')
    lb_answer['text'] = '(top+bot) * height / 2'


'''
GUI
'''
window = tk.Tk()
window.title('trapezoid')
window.geometry('1024x960')

'''
Label
'''
lb_title = tk.Label(window, text='count', font=('Times new roman', 72))
lb_title.pack()
lb_top = tk.Label(window, width=6, text='top', font=('Times New Roman', 36))
lb_top.place(x=0, y=100)
lb_bot = tk.Label(window, width=6, text='bot', font=('Times New Roman', 36))
lb_bot.place(x=0, y=200)
lb_height = tk.Label(window, width=6, text='height', font=('Time New Roman', 36))
lb_height.place(x=0, y=300)
lb_ans = tk.Label(window, text='ans', font=('Time New Roman', 36))
lb_ans.place(x=0, y=400)
lb_answer = tk.Label(window, text='(top+bot) * height / 2', font=('Time New Roman', 36))
lb_answer.place(x=200, y=400)

'''
Entry
'''
et_top = tk.Entry(window, font=('Time New Roman', 36))
et_top.place(x=200, y=100)
et_bot = tk.Entry(window, font=('Time New Roman', 36))
et_bot.place(x=200, y=200)
et_height = tk.Entry(window, font=('Time New Roman', 36))
et_height.place(x=200, y=300)

'''
Button
'''
bt_count = tk.Button(window, text='count', font=('Time New Roman', 36), command=debug)
bt_count.place(x=200, y=500)
bt_reset = tk.Button(window, text='reset', font=('Time New Roman', 36), command=reset)
bt_reset.place(x=500, y=500)

window.mainloop()
