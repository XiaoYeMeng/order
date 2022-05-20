import tkinter as tk


def en_1():
    count = int(str(lb_4['text']))
    count += int(1)
    lb_4.config(text=str(count))


def en_2():
    count = int(str(lb_4['text']))
    count -= 1
    lb_4.config(text=str(count))


def en_3():
    count = int(str(lb_5['text']))
    if count < 60:
        count += 1
    else:
        count = 0
    lb_5.config(text=str(count))


def en_4():
    count = int(str(lb_5['text']))
    if count > 0:
        count -= 1
    else:
        count = 60
    lb_5.config(text=str(count))


def en_5():
    count = int(str(lb_6['text']))
    if count < 60:
        count += 1
    else:
        count = 0
    lb_6.config(text=str(count))


def en_6():
    count = int(str(lb_6['text']))
    if count > 0:
        count -= 1
    else:
        count = 60
    lb_6.config(text=str(count))


def en_7():
    if int(lb_5['text']) == 0 and int(lb_4['text']) > 0 and int(lb_6['text']) == 0:
        lb_4['text'] = int(lb_4['text']) - 1
        lb_5['text'] = 59
        lb_6['text'] = 59
    elif int(lb_6['text']) == 0 and int(lb_5['text']) > 0:
        lb_5['text'] = int(lb_5['text']) - 1
        lb_6['text'] = 59
    elif int(lb_6['text']) > 0:
        lb_6['text'] = int(lb_6['text']) - 1
    else:
        lb_7['text'] = 'times up'
    window.after(1000, en_7)


def en_8():
    bt_1['state'] = tk.DISABLED
    bt_2['state'] = tk.DISABLED
    bt_3['state'] = tk.DISABLED
    bt_4['state'] = tk.DISABLED
    bt_5['state'] = tk.DISABLED
    bt_6['state'] = tk.DISABLED
    bt_7['state'] = tk.DISABLED


def en_9():
    bt_1['state'] = tk.NORMAL
    bt_2['state'] = tk.NORMAL
    bt_3['state'] = tk.NORMAL
    bt_4['state'] = tk.NORMAL
    bt_5['state'] = tk.NORMAL
    bt_6['state'] = tk.NORMAL
    bt_7['state'] = tk.NORMAL


'''
GUI UI
'''
window = tk.Tk()
window.title('Countdown Timer')
window.geometry('990x600')

'''
Label
'''
# title
lb_1 = tk.Label(window, text='Countdown Timer', font=('微軟正黑體', 72))
lb_1.place(x=90, y=0)
# hour:
lb_2 = tk.Label(window, text=':', font=('微軟正黑體', 72))
lb_2.place(x=370, y=120)
# min:
lb_3 = tk.Label(window, text=':', font=('微軟正黑體', 72))
lb_3.place(x=540, y=120)
# hour
lb_4 = tk.Label(window, text='00', font=('微軟正黑體', 72))
lb_4.place(x=230, y=130)
# min
lb_5 = tk.Label(window, text='00', font=('微軟正黑體', 72))
lb_5.place(x=400, y=130)
# sec
lb_6 = tk.Label(window, text='00', font=('微軟正黑體', 72))
lb_6.place(x=570, y=130)
# time's up
lb_7 = tk.Label(window, text='', font=('微軟正黑體', 36))
lb_7.place(x=400, y=420)
'''
Button
'''
# hour up
bt_1 = tk.Button(window, text='+', font=('微軟正黑體', 9), command=en_1)
bt_1.place(width=24, x=350, y=160)
# hour down
bt_2 = tk.Button(window, text='-',  font=('微軟正黑體', 9), command=en_2)
bt_2.place(width=24, x=350, y=190)
# min up
bt_3 = tk.Button(window, text='+', font=('微軟正黑體', 9), command=en_3)
bt_3.place(width=24, x=520, y=160)
# min down
bt_4 = tk.Button(window, text='-', font=('微軟正黑體', 9), command=en_4)
bt_4.place(width=24, x=520, y=190)
# sec up
bt_5 = tk.Button(window, text='+', font=('微軟正黑體', 9), command=en_5)
bt_5.place(width=24, x=690, y=160)
# sec down
bt_6 = tk.Button(window, text='-', font=('微軟正黑體', 9), command=en_6)
bt_6.place(width=24, x=690, y=190)
# start
bt_7 = tk.Button(window, width=6, text='start', font=('微軟正黑體', 36), command=lambda: [en_7(), en_8()])
bt_7.place(width=200, x=300, y=300)
# pause
bt_8 = tk.Button(window, width=6, text='pause', font=('微軟正黑體', 36), command=en_9)
bt_8.place(width=200, x=510, y=300)

window.mainloop()
