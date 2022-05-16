import tkinter as tk
window=tk.Tk()
window.title('梯形面積')
window.geometry('1024x768')


top=tk.Label(window,text='上底',fg='blue',bg='black',font=('微軟正黑體',14),width=30,height=2)        
#說明： bg為背景，font為字型，width為長，height為高，這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高
#第5步，安置標籤


bot=tk.Label(window,text='下底',fg='red',bg='black',font=('微軟正黑體',14),width=30,height=2)

#安置lable的方法有：1）l.pack();2)l.place();
#第6步，
window.configure(bg='')
window.mainloop
