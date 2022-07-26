import tkinter as tk
import dict
from tkinter import messagebox

menu = dict.dict_menu

window = tk.Tk()
window.geometry('300x100')
window.title('system')


def wm():
    window_menu = tk.Tk()
    window_menu.geometry('800x800')
    window_menu.title('目前菜單')
    lb_a = tk.Label(window_menu, text=menu['產品名稱'], font=('Time new roman', 18))
    lb_a.place(x=0, y=0)
    lb_b = tk.Label(window_menu, text=menu['產品圖片'], font=('Time new roman', 18))
    lb_b.place(x=200, y=0)
    lb_c = tk.Label(window_menu, text=menu['產品資訊'], font=('Time new roman', 18))
    lb_c.place(x=400, y=0)
    lb_d = tk.Label(window_menu, text=menu['產品價格'], font=('Time new roman', 18))
    lb_d.place(x=600, y=0)


def wd():
    window_update = tk.Tk()
    window_update.geometry('800x800')
    window_update.title('更新菜單')
    lb_name = tk.Label(window_update, text='產品名稱', font=('Time new roman', 18))
    lb_name.place(x=60, y=0)
    lb_img = tk.Label(window_update, text='產品圖片', font=('Time new roman', 18))
    lb_img.place(x=60, y=60)
    lb_info = tk.Label(window_update, text='產品資訊', font=('Time new roman', 18))
    lb_info.place(x=60, y=120)
    lb_price = tk.Label(window_update, text='產品價格', font=('Time new roman', 18))
    lb_price.place(x=60, y=180)

    et_name = tk.Entry(window_update, font=('Time new roman', 18))
    et_name.place(x=180, y=0)
    et_img = tk.Entry(window_update, font=('Time new roman', 18))
    et_img.place(x=180, y=60)
    et_info = tk.Entry(window_update, font=('Time new roman', 18))
    et_info.place(x=180, y=120)
    et_price = tk.Entry(window_update, font=('Time new roman', 18))
    et_price.place(x=180, y=180)
    bt_save = tk.Button(window_update, text='儲存', command=save_menu, font=('Time new roman', 18))
    bt_save.place(x=250, y=250)


def save_menu():
    messagebox.showinfo('menu', '儲存成功')


bt_window_menu = tk.Button(window, text='目前菜單', command=wm, font=('Time new roman', 18))
bt_window_menu.place(x=20, y=30)
bt_window_update = tk.Button(window, text='更新菜單', command=wd, font=('Time new roman', 18))
bt_window_update.place(x=170, y=30)

window.mainloop()
