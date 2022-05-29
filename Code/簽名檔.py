import tkinter as tk

'''
GUI
'''
window = tk.Tk()
window.title('title')
window.geometry('800x600')

'''
Label
'''
lb_title = tk.Label(window, text='title', font=('Time new roman', 54))
lb_title.pack()
lb_cn = tk.Label(window, text='Name(ZH)', font=('Time new roman', 36))
lb_cn.place(x=0, y=100)
lb_en = tk.Label(window, text='Name(EN)', font=('Time new roman', 36))
lb_en.place(x=0, y=200)
lb_mobile = tk.Label(window, text='Mobile', font=('Time new roman', 36))
lb_mobile.place(x=0, y=300)
lb_tel = tk.Label(window, text='Tel', font=('Time new roman', 36))
lb_tel.place(x=0, y=400)
lb_mail = tk.Label(window, text='E-mail', font=('Time new roman', 36))
lb_mail.place(x=0, y=500)

'''
Entry
'''
et_cn = tk.Entry(window, font=('Time new roman', 36))
et_cn.place(x=200, y=100)
et_en = tk.Entry(window, font=('Time new roman', 36))
et_en.place(x=200, y=200)
et_mobile = tk.Entry(window, font=('Time new roman', 36))
et_mobile.place(x=200, y=300)
et_tel = tk.Entry(window, font=('Time new roman', 36))
et_tel.place(x=200, y=400)
et_mail = tk.Entry(window, font=('Time new roman', 36))
et_mail.place(x=200, y=500)

var = tk.StringVar()
var.set('font')
test = tk.OptionMenu(window, var,  'Arial', 'Time new roman', '標楷體')
test.place(x=50, y=50)

'''
Docx
'''




window.mainloop()