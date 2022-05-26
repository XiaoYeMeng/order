import tkinter as tk


def en_1():
    lb_show['text'] = 1


'''
GUI
'''
window = tk.Tk()
window.title('count')
window.geometry('600x600')

'''
Label
'''
lb_title = tk.Label(window, text='calculator', font=('Time New Roman', 36))
lb_title.place(x=0, y=0)
lb_show = tk.Label(window, text='show', font=('Time New Roman', 27))
lb_show.place(x=0, y=50)

'''
Button
'''
bt_clear = tk.Button(window, width=2, height=1, text='ｃ', font=('Time New Roman', 18))
bt_clear.place(x=0, y=100)
bt__ = tk.Button(window, width=2, height=1, text='+/-', font=('Time New Roman', 18))
bt__.place(x=50, y=100)
bt_ratio = tk.Button(window, width=2, height=1, text='％', font=('Time New Roman', 18))
bt_ratio.place(x=100, y=100)
bt_division = tk.Button(window, width=2, height=1, text='÷', font=('Time New Roman', 18))
bt_division.place(x=150, y=100)

bt_7 = tk.Button(window, width=2, height=1, text='7', font=('Time New Roman', 18))
bt_7.place(x=0, y=150)
bt_8 = tk.Button(window, width=2, height=1, text='8', font=('Time New Roman', 18))
bt_8.place(x=50, y=150)
bt_9 = tk.Button(window, width=2, height=1, text='9', font=('Time New Roman', 18))
bt_9.place(x=100, y=150)
bt_multiplication = tk.Button(window, width=2, height=1, text='×', font=('Time New Roman', 18))
bt_multiplication.place(x=150, y=150)

bt_4 = tk.Button(window, width=2, height=1, text='4', font=('Time New Roman', 18))
bt_4.place(x=0, y=200)
bt_5 = tk.Button(window, width=2, height=1, text='5', font=('Time New Roman', 18))
bt_5.place(x=50, y=200)
bt_6 = tk.Button(window, width=2, height=1, text='6', font=('Time New Roman', 18))
bt_6.place(x=100, y=200)
bt_subtraction = tk.Button(window, width=2, height=1, text='－', font=('Time New Roman', 18))
bt_subtraction.place(x=150, y=200)

bt_1 = tk.Button(window, width=2, height=1, text='1', font=('Time New Roman', 18), command=en_1)
bt_1.place(x=0, y=250)
bt_2 = tk.Button(window, width=2, height=1, text='2', font=('Time New Roman', 18))
bt_2.place(x=50, y=250)
bt_3 = tk.Button(window, width=2, height=1, text='3', font=('Time New Roman', 18))
bt_3.place(x=100, y=250)
bt_addition = tk.Button(window, width=2, height=1, text='＋', font=('Time New Roman', 18))
bt_addition.place(x=150, y=250)

bt_0 = tk.Button(window, width=2, height=1, text='0', font=('Time New Roman', 18))
bt_0.place(x=0, y=300)
bt_ = tk.Button(window, width=2, height=1, text='( )', font=('Time New Roman', 18))
bt_.place(x=50, y=300)
bt_dot = tk.Button(window, width=2, height=1, text='.', font=('Time New Roman', 18))
bt_dot.place(x=100, y=300)
bt_equal = tk.Button(window, width=2, height=1, text='＝', font=('Time New Roman', 18))
bt_equal.place(x=150, y=300)

window.mainloop()
