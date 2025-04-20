from tkinter import *
import tkinter as tk
wd = Tk()
wd.title('เครื่องคิดเลข')
wd.minsize(400,400)
wd.configure(bg='#FFFFCC')
def R():
    g = float(Input.get())
    t = float(Input2.get())
    r = float(g-t)
    output = float('%.2f'%r)

    Output.configure(text=output)

def B():
    g = float(Input.get())
    t = float(Input2.get())
    r = float(g+t)
    output = float('%.2f'%r)

    Output.configure(text=output)
    
def T():
    g = float(Input.get())
    t = float(Input2.get())
    r = float(g/t)
    output = float('%.2f'%r)

    Output.configure(text=output)

def U():
    g = float(Input.get())
    t = float(Input2.get())
    r = float(g*t)
    output = str('%.2f'%r)

    Output.configure(text=output)

def Y():
    g = float(Input.get())
    r = float(g*g)
    output = str('%.2f'%r)

    Output.configure(text=output)

def I():
    g = float(Input.get())
    t = float(Input2.get())
    r = float(g**t)
    output = str('%.2f'%r)

    Output.configure(text=output)

def f(n):
    
     f = 1

     for i in range(1,n+1):
        f = (f*i)
     return f

def F():
    g = f(int(Input.get()))
    output = float('%.2f'%g)

    Output.configure(text=output)

def S():
    Label(wd,text='ข้อ 1',bg ='#FFFFCC',fg='#990000').place(x=100,y=100)
    Label(wd,text='ข้อ 2',bg ='#FFFFCC',fg='#990000').place(x=170,y=100)
    Label(wd,text='ข้อ 3',bg ='#FFFFCC',fg='#990000').place(x=240,y=100)
    Entry(wd,width=10).place(x=240,y=130)
    Entry(wd,width=10).place(x=100,y=130)
    Entry(wd,width=10).place(x=170,y=130)
  

def C():
    output = ' '

    Output.configure(text=output)

    

Input = Entry(wd,width=30)
Input.place(x=100,y=0)

Input2 = Entry(wd,width=30)
Input2.place(x=100,y=20)

enter = Button(wd,text='-',command=R,bg='#FFCC33',width=3)
enter.grid(row=3,column=1)

enter2 = Button(wd,text='+',command=B,bg='#FFCC33',width=3)
enter2.grid(row=3,column=0)

enter3 = Button(wd,text='/',command=T,bg='#FFCC33',width=3)
enter3.grid(row=4,column=0)

enter3 = Button(wd,text='*',command=U,bg='#FFCC33',width=3)
enter3.grid(row=4,column=1)

enter4 = Button(wd,text=' *2',command=Y,bg='#FFCC33',width=3)
enter4.grid(row=5,column=0)

enter4 = Button(wd,text=' **',command=I,bg='#FFCC33',width=3)
enter4.grid(row=5,column=1)

enter5 = Button(wd,text='!',command=F,bg='#FFCC33',width=3)
enter5.grid(row=6,column=0)

enter6 = Button(wd,text='C',command=C,bg='#FFCC33',width=3)
enter6.grid(row=3,column=3)

enter7 = Button(wd,text='เซฟ',command=S,bg='#FFCC33',width=3)
enter7.place(x=60,y=122)


text = Label(wd,text='แสดงผล',bg ='#FFFFCC',fg='#990000')
text.place(x=175,y=40)

Output = Label(wd,bg='#FFFFCC')
Output.place(x=180,y=60)


#if __name__ =='__main__':
    #r()
wd.mainloop() 
