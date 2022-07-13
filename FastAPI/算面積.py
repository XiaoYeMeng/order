import tkinter as tk
from tkinter import messagebox
import requests

window = tk.Tk()
window.geometry('600x400')

http = 'http://192.168.2.113:8888/'
circle = 'circle?radius='
rectangle_long = 'rectangle?long='
rectangle_width = '&width='
triangle_bot = 'triangle?bot='
triangle_height = '&height='
#

def count_circle():
    # 計算圓形面積
    try:
        float(et_radius.get())

    except ValueError:
        messagebox.showerror('error', 'Enter a value.')
    else:
        count = requests.post(http + circle + et_radius.get() + '')
        answer = count.json()
        lb_answer['text'] = answer


def count_rectangle():
    # 計算矩形面積
    try:
        float(et_long.get())
        float(et_width.get())
    except ValueError:
        messagebox.showerror('error', 'Enter a value.')
    else:
        count = requests.post(http + rectangle_long + et_long.get() + rectangle_width + et_width.get() + '')
        answer = count.json()
        lb_answer['text'] = answer


def count_triangle():
    # 計算三角形面積
    try:
        float(et_bot.get())
        float(et_height.get())
    except ValueError:
        messagebox.showerror('error', 'Enter a value.')
    else:
        count = requests.post(http + triangle_bot + et_bot.get() + triangle_height + et_height.get() + '')
        answer = count.json()
        lb_answer['text'] = answer


'''
Label
'''
lb_answer = tk.Label(window, text='answer', font=('Time new roman', 36))
lb_answer.grid(column=1, row=0)

'''
Entry
'''
et_radius = tk.Entry(window, width=6,  font=('Time new roman', 36))
et_radius.grid(column=1, row=1)

et_long = tk.Entry(window, width=6,  font=('Time new roman', 36))
et_long.grid(column=1, row=2)
et_width = tk.Entry(window, width=6,  font=('Time new roman', 36))
et_width.grid(column=2, row=2)

et_bot = tk.Entry(window, width=6, font=('Time new roman', 36))
et_bot.grid(column=1, row=3)
et_height = tk.Entry(window, width=6, font=('Time new roman', 36))
et_height.grid(column=2, row=3)

'''
Button
'''
bt_circle = tk.Button(window, text='圓形', width=6, height=1, command=count_circle, font=('Time new roman', 36))
bt_circle.grid(column=0, row=1)

bt_rectangle = tk.Button(window, text='矩形', width=6, command=count_rectangle, font=('Time new roman', 36))
bt_rectangle.grid(column=0, row=2)

bt_triangle = tk.Button(window, text='三角形', width=6, command=count_triangle, font=('Time new roman', 36))
bt_triangle.grid(column=0, row=3)

window.mainloop()
