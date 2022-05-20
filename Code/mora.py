import tkinter as tk
import random
from PIL import Image, ImageTk


def scissors_result():
    pc = random.choice(['scissors', 'rock', 'paper'])
    lb_user['image'] = img_scissors
    if pc == 'scissors':
        lb_pc['image'] = img_scissors
        lb_result['text'] = 'tie'
    elif pc == 'rock':
        lb_pc['image'] = img_rock
        lb_result['text'] = 'lose'
    else:
        lb_pc['image'] = img_paper
        lb_result['text'] = 'win'


def rock_result():
    pc = random.choice(['scissors', 'rock', 'paper'])
    lb_user['image'] = img_rock
    if pc == 'scissors':
        lb_pc['image'] = img_scissors
        lb_result['text'] = 'win'
    elif pc == 'rock':
        lb_pc['image'] = img_rock
        lb_result['text'] = 'tie'
    else:
        lb_pc['image'] = img_paper
        lb_result['text'] = 'lose'


def paper_result():
    pc = random.choice(['scissors', 'rock', 'paper'])
    lb_user['image'] = img_paper
    if pc == 'scissors':
        lb_pc['image'] = img_scissors
        lb_result['text'] = 'lose'
    elif pc == 'rock':
        lb_pc['image'] = img_rock
        lb_result['text'] = 'win'
    else:
        lb_pc['image'] = img_paper
        lb_result['text'] = 'tie'


'''
GUI
'''
window = tk.Tk()
window.title('mora')
window.geometry('800x600')

'''
Image
'''
img_scissors = ImageTk.PhotoImage(Image.open('./image/scissors.jpg'))
img_rock = ImageTk.PhotoImage(Image.open('./image/rock.jpg'))
img_paper = ImageTk.PhotoImage(Image.open('./image/paper.jpg'))
'''
Label
'''
lb_title = tk.Label(window, width=6, text='mora', font=('Time New Roman', 72))
lb_title.pack()
lb_user = tk.Label(window, text=' user', font=('Time New Roman', 36))
lb_user.place(x=100, y=200)
lb_pc = tk.Label(window, text='  pc', font=('Time New Roman', 36))
lb_pc.place(x=300, y=200)
lb_result = tk.Label(window, width=6, text='result', font=('Time New Roman', 36))
lb_result.place(x=500, y=200)

'''
Button
'''
lb_scissors = tk.Button(window, image=img_scissors,  font=('Time New Roman', 36), command=scissors_result)
lb_scissors.place(x=100, y=400)
lb_rock = tk.Button(window, image=img_rock,  font=('Time New Roman', 36), command=rock_result)
lb_rock.place(x=300, y=400)
lb_paper = tk.Button(window, image=img_paper,  font=('Time New Roman', 36), command=paper_result)
lb_paper.place(x=500, y=400)

window.mainloop()
