import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('800x600')
window.title('window')

topic_1 = ['第一題 : 1 + 1 = ?', '1', '4', '3', '2']
topic_2 = ['第二題 : 2 + 2 = ?', '2', '6', '4', '11']
topic_3 = ['第三題 : 4 + 4 = ?', '20', '8', '6', '11']
topic_4 = ['第四題 : 8 + 8 = ?', '16', '19', '15', '13']


def start():
    if lb_q['text'] == '等待開始中' or lb_q['text'] == 'end':
        lb_q['text'] = topic_1[0]
        lb_ans['text'] = int(0)
        bt_a['text'] = topic_1[1]
        bt_b['text'] = topic_1[2]
        bt_c['text'] = topic_1[3]
        bt_d['text'] = topic_1[4]
    else:
        messagebox.showerror('error', '請先結束作答')


def a():
    if lb_q['text'] == topic_4[0] and bt_a['text'] == topic_4[1]:
        messagebox.showinfo('result', 'true')
        lb_ans['text'] += 25
        lb_q['text'] = 'end'
        messagebox.showinfo('總分數', str(lb_ans['text']) + ' 分')
    elif lb_q['text'] == topic_1[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_2[0]
        bt_a['text'] = topic_2[1]
        bt_b['text'] = topic_2[2]
        bt_c['text'] = topic_2[3]
        bt_d['text'] = topic_2[4]
    elif lb_q['text'] == topic_2[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_3[0]
        bt_a['text'] = topic_3[1]
        bt_b['text'] = topic_3[2]
        bt_c['text'] = topic_3[3]
        bt_d['text'] = topic_3[4]
    elif lb_q['text'] == topic_3[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_4[0]
        bt_a['text'] = topic_4[1]
        bt_b['text'] = topic_4[2]
        bt_c['text'] = topic_4[3]
        bt_d['text'] = topic_4[4]
    else:
        messagebox.showerror('error', '請先點選 start')


def b():
    if lb_q['text'] == topic_3[0] and bt_b['text'] == topic_3[2]:
        messagebox.showinfo('result', 'true')
        lb_ans['text'] += 25
        lb_q['text'] = topic_4[0]
        bt_a['text'] = topic_4[1]
        bt_b['text'] = topic_4[2]
        bt_c['text'] = topic_4[3]
        bt_d['text'] = topic_4[4]
    elif lb_q['text'] == topic_1[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_2[0]
        bt_a['text'] = topic_2[1]
        bt_b['text'] = topic_2[2]
        bt_c['text'] = topic_2[3]
        bt_d['text'] = topic_2[4]
    elif lb_q['text'] == topic_2[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_3[0]
        bt_a['text'] = topic_3[1]
        bt_b['text'] = topic_3[2]
        bt_c['text'] = topic_3[3]
        bt_d['text'] = topic_3[4]
    elif lb_q['text'] == topic_4[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = 'end'
        messagebox.showinfo('總分數', str(lb_ans['text']) + ' 分')
    else:
        messagebox.showerror('error', '請先點選 start')


def c():
    if lb_q['text'] == topic_2[0] and bt_c['text'] == topic_2[3]:
        messagebox.showinfo('result', 'true')
        lb_ans['text'] += 25
        lb_q['text'] = topic_3[0]
        bt_a['text'] = topic_3[1]
        bt_b['text'] = topic_3[2]
        bt_c['text'] = topic_3[3]
        bt_d['text'] = topic_3[4]
    elif lb_q['text'] == topic_1[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_2[0]
        bt_a['text'] = topic_2[1]
        bt_b['text'] = topic_2[2]
        bt_c['text'] = topic_2[3]
        bt_d['text'] = topic_2[4]
    elif lb_q['text'] == topic_3[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_4[0]
        bt_a['text'] = topic_4[1]
        bt_b['text'] = topic_4[2]
        bt_c['text'] = topic_4[3]
        bt_d['text'] = topic_4[4]
    elif lb_q['text'] == topic_4[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = 'end'
        messagebox.showinfo('總分數', str(lb_ans['text']) + ' 分')
    else:
        messagebox.showerror('error', '請先點選 start')


def d():
    if lb_q['text'] == topic_1[0] and bt_d['text'] == topic_1[4]:
        messagebox.showinfo('result', 'true')
        lb_ans['text'] += 25
        lb_q['text'] = topic_2[0]
        bt_a['text'] = topic_2[1]
        bt_b['text'] = topic_2[2]
        bt_c['text'] = topic_2[3]
        bt_d['text'] = topic_2[4]
    elif lb_q['text'] == topic_2[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_3[0]
        bt_a['text'] = topic_3[1]
        bt_b['text'] = topic_3[2]
        bt_c['text'] = topic_3[3]
        bt_d['text'] = topic_3[4]
    elif lb_q['text'] == topic_3[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = topic_4[0]
        bt_a['text'] = topic_4[1]
        bt_b['text'] = topic_4[2]
        bt_c['text'] = topic_4[3]
        bt_d['text'] = topic_4[4]
    elif lb_q['text'] == topic_4[0]:
        messagebox.showerror('result', 'false')
        lb_q['text'] = 'end'
        messagebox.showinfo('總分數', str(lb_ans['text']) + ' 分')
    else:
        messagebox.showerror('error', '請先點選 start')


lb_q = tk.Label(window, text='等待開始中', font=('Time new roman', 18))
lb_q.pack()
bt_start = tk.Button(window, text='start', command=start, font=('Time new roman', 18))
bt_start.pack()
bt_a = tk.Button(window, text='a', command=a, font=('Time new roman', 18))
bt_a.pack()
bt_b = tk.Button(window, text='b', command=b, font=('Time new roman', 18))
bt_b.pack()
bt_c = tk.Button(window, text='c', command=c, font=('Time new roman', 18))
bt_c.pack()
bt_d = tk.Button(window, text='d', command=d, font=('Time new roman', 18))
bt_d.pack()
lb_ans = tk.Label(window, text=int(0), font=('Time new roman', 18))
lb_ans.pack()

window.mainloop()