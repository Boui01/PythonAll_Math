import random
import webbrowser
from tkinter import *
import tkinter as tk
root = Tk()
root.title('ค้นหาสิ')
root.minsize(width=400,height=400)
canvas = Canvas(root,width=500,height=500)
canvas.place(x=-100,y=-50)
pt = PhotoImage(file=r'C:\Users\Administrator.AIO-20200809NZH\Downloads\กูเอง\4.png')
canvas.create_image(300,300,image=pt,anchor=CENTER)
def helps():
    h = 'sbc ---> เว็ป รร.'+'\n'+'song ---> เพลง'+'\n'+'book ---> สูตรต่างๆ'+'\n'+\
        'save ---> รูปภาพ'
    op1.configure(text=h)
def school():
    webbrowser.open('https://reg.southeast.ac.th/registrar/home.asp')
    c = ' '
    op1.configure(text=c)
def book():
    def alls():
        f = open(r'C:\Users\Administrator.AIO-20200809NZH\AppData\Local\Programs\Python\Python39\save\text\สูตรรวม.txt', 'r',encoding='utf-8')
        print(f.read())
        f.close
    def PGALL():
        import PGALL as pg
        pg.grid()
        pg.Ca()
        pg.CLASS()
    def POP():
        import pop
        pop.Ftr1()
    bt1 = Button(root,text='สูตรทั้งหมด',command=alls,bg='#FFCC99')
    bt1.place(x=10,y=130)
    bt2 = Button(root,text='PGALL',command=PGALL,bg='#FFCC99')
    bt2.place(x=100,y=130)
    bt1 = Button(root,text='POP',command=POP,bg='#FFCC99')
    bt1.place(x=190,y=130)

    c = ' '
    op1.configure(text=c)
def song():
    w = ['https://www.youtube.com/watch?v=w-RzNzsaZvs&list=PLTeY7bC32TdYsjRX5G583mKsATOfpvq2S&index=1',\
         'https://www.youtube.com/watch?v=8y5wmdM4vBg&list=PLTeY7bC32TdbYbVR7oeZhetnYZtixKNxK&index=1'\
         ,'https://www.youtube.com/watch?v=cqA58xa-Duw&list=PLTeY7bC32TdZDCjT4Kp4rKvYIgEVRv-gq&index=2']
    e = random.choice(w)
    webbrowser.open(e)
    c = ' '
    op1.configure(text=c)
def photo():
    import cv2
    img = cv2.imread('2.png',cv2.IMREAD_COLOR)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    c = ' '
    op1.configure(text=c)
def save():
    
    w = r'C:\Users\Administrator.AIO-20200809NZH\AppData\Local\Programs\Python\Python39\save'

    op1.configure(text=w)
def sh():
    w = str(et1.get())
    so = 'song'
    s = 'save'
    p = 'photo'
    b = 'book'
    sbc = 'sbc'
    e = song()if w==so else save()if  w==s else photo()if w==p else book() \
        if w==b else school() if w==sbc else helps()

    op1.configure(text=e)

   
root.option_add("*Font",'consolas 12')
lb1 = Label(root,text='ใส่รหัสสิ',fg='#990000').pack()
et1 = Entry(root,width=10)
et1.pack(pady=10)

bt1 = Button(root,text='unrlock',command=sh,bg='#FFCCCC',cursor='gumby')
bt1.pack(pady=10)
op1 = Label(root,bg='#f1d8db')
op1.pack()


root.mainloop()
