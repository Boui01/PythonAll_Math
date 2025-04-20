import tkinter as tk
import pyautogui as pg
import time

def TIME():
    output = '5 วิ'+'  ==>'+' 1'+'\n'+'10 วิ'+'  ==>'+' 2'+'\n'+' 15 วิ'+'  ==>'+' 3'+\
             '\n'+' 20 วิ'+'  ==>'+' 3'+'\n'+' 25 วิ'+'  ==>'+' 4'+'\n'+' 30 วิ'+\
             '  ==>'+' 5'+'\n'+' 35 วิ'+'  ==>'+' 6'+'\n'+' 40 วิ'+'  ==>'+' 7'\
             +'\n'+' 45 วิ'+'  ==>'+' 8'+'\n'+' 50 วิ'+'  ==>'+' 9'+'\n'+' 55 วิ'\
             +'  ==>'+' 10'+'\n'+' 60 วิ'+'  ==>'+' 11'
    output1.configure(text=output)
    
def afk(n):
    time.sleep(3)
    for i in range(n):
        result = pg.position(1583,458)
        result2 = pg.position(14,369)
        pg.moveTo(result,duration=2)
        pg.moveTo(result2,duration=2)
        
def AFK():
    a = afk(int(input0.get()))
    c = int(input0.get())
    b = '5' if c==1 else '10' if c==2 else '15' if c==3 else \
        '20' if c==4 else '25' if c==5 else '30' if c==6 else '35' \
        if c==7 else '40'if c==8 else '45' if c==9 else '50' if c==10 \
        else '55' if c==11 else '60'

    output = str(b)+'  วิ'

    output0.configure(text=output)

W = tk.Tk()
W.title('AFK')
W.minsize(width=400,height=400)
W.configure(background='#FFCCCC')

text = tk.Label(master=W,text='ตาราง',bg='#FFCCCC',fg='#333333')
text.pack()

button = tk.Button(master=W,text='ทำงาน',width=10,bg='#FFCC99',command=TIME)
button.pack(pady=10)

text = tk.Label(master=W,text='ใส่เวลา',bg='#FFCCCC',fg='#333333')
text.pack()

input0 = tk.Entry(master=W)
input0.pack(pady=10)

button1 = tk.Button(master=W,text='ทำงาน',width=10,bg='#FFCC99',command=AFK)
button1.pack(pady=10)

output1 = tk.Label(master=W,bg='#FFCCCC')
output1.pack(pady=10)

output0 = tk.Label(master=W,bg='#FFCCCC')
output0.pack(pady=10)

W.mainloop()
