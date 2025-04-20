from tkinter import *
import tkinter as tk
wd = Tk()
wd.title('ตรรกศาตร์')
wd.minsize(400,400)
wd.configure(bg='#FFFFCC')
canvas = Canvas(wd,width=500,height=500)
canvas.place(x=-100,y=-80)
pt = PhotoImage(file=r'C:\Users\Administrator.AIO-20200809NZH\Downloads\กูเอง\1.png')
canvas.create_image(300,300,image=pt,anchor=CENTER)

show2 = StringVar()
def And():
        right = str(Right.get())
        left = str(Left.get())
        ShowRight = right
        ShowLeft = left
        ShowT = str('T')
        ShowF = str('F')
        ShowMid.configure(text="And")

        if "T"==left and"T"==right:
            Show1.configure(text=ShowT)
            Showright.configure(text=ShowRight)
            Showleft.configure(text=ShowLeft)
        elif(""==left and ""==right):
            Show1.configure(text="")
            Showright.configure(text=ShowRight)
            Showleft.configure(text=ShowLeft)
        else:
            Show1.configure(text=ShowF)
            Showright.configure(text=ShowRight)
            Showleft.configure(text=ShowLeft)
        
def Or():
        right = str(Right.get())
        left = str(Left.get())
        ShowRight = right
        ShowLeft = left
        ShowT = str('T')
        ShowF = str('F')
        ShowMid.configure(text="Or")
        if "F"==left and "F"==right:
             Show1.configure(text=ShowF)
             Showright.configure(text=ShowRight)
             Showleft.configure(text=ShowLeft)
        elif(""==left and ""==right):
            Show1.configure(text="")
            Showright.configure(text=ShowRight)
            Showleft.configure(text=ShowLeft)
        else:
             Show1.configure(text=ShowT)
             Showright.configure(text=ShowRight)
             Showleft.configure(text=ShowLeft)        

def If_else():
        right = str(Right.get())
        left = str(Left.get())
        ShowRight = right
        ShowLeft = left
        ShowT = str('T')
        ShowF = str('F')
        ShowMid.configure(text="-->")

        if "T"==left and "F"==right:
             Show1.configure(text=ShowF)
             Showright.configure(text=ShowRight)
             Showleft.configure(text=ShowLeft)    
        elif(""==left and ""==right):
            Show1.configure(text="")
            Showright.configure(text=ShowRight)
            Showleft.configure(text=ShowLeft)
        else:
             Show1.configure(text=ShowT)
             Showright.configure(text=ShowRight)
             Showleft.configure(text=ShowLeft)  


def Before():
        right = str(Right.get())
        left = str(Left.get())
        ShowRight = right
        ShowLeft = left
        ShowT = str('T')
        ShowF = str('F')
        ShowMid.configure(text="<-->") 
        if "T"==left and "T"==right:
             Show1.configure(text=ShowT)
             Showright.configure(text=ShowRight)
             Showleft.configure(text=ShowLeft)  
        elif "F"==left and "F"==right:
             Show1.configure(text=ShowT)
             Showright.configure(text=ShowRight)
             Showleft.configure(text=ShowLeft)
        elif(""==left and ""==right):
            Show1.configure(text="")
            Showright.configure(text=ShowRight)
            Showleft.configure(text=ShowLeft)  
        else:
             Show1.configure(text=ShowF)
             Showright.configure(text=ShowRight)
             Showleft.configure(text=ShowLeft)  

def returnrightT():
    Right.delete(0,2)
    Right.insert(0,"T")
    Left.delete(0,2)
def returnrightF():
    Right.delete(0,2)
    Right.insert(0,"F")
    Left.delete(0,2)


def returnleftT():
    Left.delete(0,2)
    Left.insert(0,"T")
    Right.delete(0,2)
def returnleftF():
    Left.delete(0,2)
    Left.insert(0,"F")
    Right.delete(0,2)

def notright():
    right = str(Right.get())
    if "T"==right:
        Right.delete(0,2)
        Right.insert(0,"F")
    else:
        Right.delete(0,2)
        Right.insert(0,"T")

def notleft():
    left = str(Left.get())
    if "T"==left:
        Left.delete(0,2)
        Left.insert(0,"F")
    else:
        Left.delete(0,2)
        Left.insert(0,"T")

Right = Entry(wd,width=10)
Right.place(x=250,y=20)

Left = Entry(wd,width=10)
Left.place(x=63,y=20)

AndShow = Button(wd,text='and',command=And,bg='#FFCC33',width=3,relief=RIDGE)
AndShow.place(x=185,y=20)

OrShow = Button(wd,text='or',command=Or,bg='#FFCC33',width=3,relief=RIDGE)
OrShow.place(x=185,y=60)

IfShow = Button(wd,text='If_else',command=If_else,bg='#FFCC33',width=5,relief=RIDGE)
IfShow.place(x=180,y=100)

BeforeShow = Button(wd,text='Before',command=Before,bg='#FFCC33',width=5,relief=RIDGE)
BeforeShow.place(x=180,y=140)

Bg = Label(wd,text=' ',bg ='#fff0e3',fg='#990000',width=30,height=8)
Bg.place(x=100,y=200)

Show1 = Label(wd,text='_',bg ='#fff0e3',fg='#990000',font = ("Helvetica", 20))
Show1.place(x=190,y=200)

Show2 = Label(wd,text='_',bg ='#fff0e3',fg='#990000',textvariable=show2)
Show2.place(x=0,y=200)

Showright = Label(wd,text='_',bg ='#fff0e3',fg='#990000',font = ("Helvetica",20))
Showright.place(x=240,y=250)

Showleft = Label(wd,text='_',bg ='#fff0e3',fg='#990000',font = ("Helvetica",20))
Showleft.place(x=140,y=250)

ShowMid = Label(wd,text='',bg ='#fff0e3',fg='#990000',font = ("Helvetica",20))
ShowMid.place(x=180,y=250)

Notright = Button(wd,text='~',bg='#d7dcbe',width=2,relief=RIDGE,command=notright)
Notright.place(x=317,y=20)

Notleft = Button(wd,text='~',bg='#d7dcbe',width=2,relief=RIDGE,command=notleft)
Notleft.place(x=130,y=20)

ReturnRight = Menubutton(wd,text='ReturnRight',bg='#FFCC33',width=10,relief=RIDGE)
ReturnRight.menu = Menu(ReturnRight,tearoff=0)
ReturnRight['menu']=ReturnRight.menu
ReturnRight.menu.add_command(label='T',command=returnrightT)
ReturnRight.menu.add_command(label='F',command=returnrightF)
ReturnRight.place(x=250,y=200)


ReturnLeft = Menubutton(wd,text='ReturnRight',bg='#FFCC33',width=10,relief=RIDGE)
ReturnLeft.menu = Menu(ReturnLeft,tearoff=0)
ReturnLeft['menu']=ReturnLeft.menu
ReturnLeft.menu.add_command(label='T',command=returnleftT)
ReturnLeft.menu.add_command(label='F',command=returnleftF)
ReturnLeft.place(x=100,y=200)

wd.mainloop()