import tkinter as tk
import time


def en_1():

    count = int(str(lb_4['text']))
    count += 1
    lb_4.config(text=str(count))


def en_2():
    count = int(str(lb_4['text']))
    count -= 1
    lb_4.config(text=str(count))


def en_3():
    count = int(str(lb_5['text']))
    count += 1
    lb_5.config(text=str(count))


def en_4():
    count = int(str(lb_5['text']))
    count -= 1
    lb_5.config(text=str(count))


def en_5():
    count = int(str(lb_6['text']))
    count += 1
    lb_6.config(text=str(count))


def en_6():
    count = int(str(lb_6['text']))
    count -= 1
    lb_6.config(text=str(count))


'''
GUI UI
'''
window = tk.Tk()
window.title('countdown timer')
window.geometry('990x600')

'''
Label
'''
# title
lb_1 = tk.Label(text='countdown timer', font=('微軟正黑體', 72))
lb_1.place(x=90, y=0)
# hour:
lb_2 = tk.Label(text=':', font=('微軟正黑體', 72))
lb_2.place(x=370, y=120)
# min:
lb_3 = tk.Label(text=':', font=('微軟正黑體', 72))
lb_3.place(x=540, y=120)
# hour
lb_4 = tk.Label(text='00', font=('微軟正黑體', 72))
lb_4.place(x=230, y=130)
# min
lb_5 = tk.Label(text='00', font=('微軟正黑體', 72))
lb_5.place(x=400, y=130)
# sec
lb_6 = tk.Label(text='00', font=('微軟正黑體', 72))
lb_6.place(x=570, y=130)

'''
Button
'''
# hour up
bt_1 = tk.Button(text='+', font=('微軟正黑體', 9), command=en_1)
bt_1.place(width=24, x=350, y=160)
# hour down
bt_2 = tk.Button(text='-',  font=('微軟正黑體', 9), command=en_2)
bt_2.place(width=24, x=350, y=190)
# min up
bt_3 = tk.Button(text='+', font=('微軟正黑體', 9), command=en_3)
bt_3.place(width=24, x=520, y=160)
# min down
bt_4 = tk.Button(text='-', font=('微軟正黑體', 9), command=en_4)
bt_4.place(width=24, x=520, y=190)
# sec up
bt_5 = tk.Button(text='+', font=('微軟正黑體', 9), command=en_5)
bt_5.place(width=24, x=690, y=160)
# sec down
bt_6 = tk.Button(text='-', font=('微軟正黑體', 9), command=en_6)
bt_6.place(width=24, x=690, y=190)
# start
bt_7 = tk.Button(width=6, text='start', font=('微軟正黑體', 36))
bt_7.place(width=200, x=300, y=300)
# pause
bt_8 = tk.Button(width=6, text='pause', font=('微軟正黑體', 36))
bt_8.place(width=200, x=510, y=300)


window.mainloop()
