import tkinter as tk
from tkinter import messagebox
import requests

window = tk.Tk()
window.geometry('600x400')
window.title('data')

http = 'http://192.168.2.113:8888/data?name='
mail = '&mail='
m_tel = '&m_tel='
tel = '&tel='
address = '&address='


def send():

    requests.post(http + et_name.get() + mail + et_mail.get() +
                  m_tel + et_m_tel.get() + tel + et_tel.get() + address + et_address.get())
    messagebox.showinfo('message', '傳送成功')

'''
Label
'''
lb_name = tk.Label(window, text='姓名 :', font=('Time new roman', 18))
lb_name.place(x=0, y=50)
lb_mail = tk.Label(window, text='信箱 :', font=('Time new roman', 18))
lb_mail.place(x=0, y=100)
lb_m_tel = tk.Label(window, text='手機 :', font=('Time new roman', 18))
lb_m_tel.place(x=0, y=150)
lb_tel = tk.Label(window, text='電話 :', font=('Time new roman', 18))
lb_tel.place(x=0, y=200)
lb_address = tk.Label(window, text='地址 :', font=('Time new roman', 18))
lb_address.place(x=0, y=250)

'''
Entry
'''
et_name = tk.Entry(window, width=18, font=('Time new roman', 18))
et_name.place(x=80, y=50)
et_mail = tk.Entry(window, width=18, font=('Time new roman', 18))
et_mail.place(x=80, y=100)
et_m_tel = tk.Entry(window, width=18, font=('Time new roman', 18))
et_m_tel.place(x=80, y=150)
et_tel = tk.Entry(window, width=18, font=('Time new roman', 18))
et_tel.place(x=80, y=200)
et_address = tk.Entry(window, width=18, font=('Time new roman', 18))
et_address.place(x=80, y=250)

'''
Button
'''
bt_send = tk.Button(window, text='傳送', width=9, command=send, font=('Time new roman', 18))
bt_send.place(x=80, y=300)

window.mainloop()
