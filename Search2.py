from tkinter import Tk,Menu,Label
import random
import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import filedialog
root = Tk()
root.title('ค้นหาสิ')
root.minsize(width=400,height=400)
root.configure(background='#f1d8db')
def new():
    root = Tk()
    root.title('ค้นหาสิ')
    root.minsize(width=400,height=400)
    root.configure(background='#f1d8db')
    def app():
        webbrowser.open('https://www.youtube.com/watch?v=mCdaP4-DLjM')
    def classroom():
        def Math():
            webbrowser.open('https://classroom.google.com/u/3/c/MzcwMjUwMTI5OTU0')
        def THAI():
            webbrowser.open('https://classroom.google.com/u/3/c/MzcwNDkxNzc3MDk4')
        def MATH():
            webbrowser.open('https://classroom.google.com/u/3/c/MzcwNjQ4NTIxNzY2')
        def TN():
            webbrowser.open('https://classroom.google.com/u/0/c/MjI2MzA5NDM4NjU4')
        def PG():
            webbrowser.open('https://classroom.google.com/u/0/c/MzcxNDY3MjIzMDY3')   
        bt1 = Button(root,text='คณิตสถิติ',command=Math,bg='#FFCC99',font=('Tahoma',10)).place(x=10,y=130)
        Button(root,text='ภาษาไทย',command=THAI,bg='#FFCC99',font=('Tahoma',10)).place(x=100,y=130)
        Button(root,text='คณิตพื้นฐาน',command=MATH,bg='#FFCC99',font=('Tahoma',10)).place(x=190,y=130)
        Button(root,text='เทคโนโลยี',command=TN,bg='#FFCC99',font=('Tahoma',10)).place(x=300,y=130)
        c = ' '
        op1.configure(text=c)
    def helps():
        h = 'sbc ---> เว็ป รร.'+'\n'+'song ---> เพลง'+'\n'+'book ---> สูตรต่างๆ'+'\n'+\
        'save ---> รูปภาพ'+'\n'+'classroom ---> ชั้นเรียน'
        op1.configure(text=h)
    def school():
        webbrowser.open('https://reg.southeast.ac.th/registrar/home.asp')
        c = ' '
        op1.configure(text=c)
    def book():
        def alls():
            f = open(r'C:\Users\Administrator.AIO-20200809NZH\AppData\Local\Programs\Python\Python39\save\text\สูตรรวม.txt', 'r',encoding='utf-8')
            s = f.read()
            my_text.insert(END,s)
            f.close
        my_text = Text(root,width=50,height=20)
        my_text.pack(pady=20)
        def POP():
            import pop
            pop.Ftr1()

        bt2 = Button(root,text='สูตรทั้งหมด',command=alls,bg='#FFCC99')
        bt2.place(x=10,y=130)
        bt4 = Button(root,text='POP',command=POP,bg='#FFCC99')
        bt4.place(x=150,y=130)

        c = ' '
        op1.configure(text=c)
############################################PGALL##############################
    def PGALL():
        root = Tk()
        root.title('สูตรรวม')
        root.minsize(width=400,height=400)
        root.configure(background='#f1d8db')
    
#--------------------------------------CLASS------------------------------------
        def CLASS():
            def Md():
                output = ('คาบเช้า 9.00-12.00'+'\n'+'\n'+'166-016-408-3'+'\n'+'อาจารย์ สุณี ทิพย์เกษร'+'\n'\
                     +'\n'+'--------------------'+'\n' +'คาบบ่าย 13.00-16.00'+'\n'+'\n'+'166-077-9779'+'\n'+'อาจารย์ สุชาติ รมณียารักษ์')
                Q_output.configure(text=output)
            def Td():
                output = ('คาบเช้า 9.00-12.00'+'\n'+'\n'+'166-997-585-2'+'\n'+'อาจารย์ บริสุทธิ์ ผึ่งผดุง'+'\n'\
                     +'\n'+'--------------------'+'\n' +'คาบบ่าย 13.00-16.00'+'\n'+'\n'+'918-000-519'+'\n'+\
                  'ผู้ช่วยศาสตราจารย์ ดร.อาจารย์ รวมพร ทองรัศมี')
                Q_output.configure(text=output)
            def Trd():
                output = ('คาบเช้า 9.00-12.00'+'\n'+'\n'+'166-828-062-5'+'\n'+'อาจารย์ อภิชิต เสมศรี'+'\n'\
                     +'\n'+'--------------------'+'\n' +'คาบบ่าย 13.00-16.00'+'\n'+'\n'+'166-594-7544'+'\n'+\
                  'ดร.ธีรพล ลิ้มศรัทธา')
                Q_output.configure(text=output)
        
            window = tk.Tk()
            window.title('ตารางเรียน ปี 64')
            window.minsize(width=400,height=400)
            window.configure(background='#FFFFCC')
    
            Q_label = tk.Label(master=window,text='วันจันทร์',bg='#FFFFCC',fg='#990000')
            Q_label.pack()
    
            Q_button = tk.Button(master=window,text='แสดง',width=10,command=Md,bg='#FFCC99')
            Q_button.pack(pady=10)
        
            Q_label2 = tk.Label(master=window,text='วันอังคาร',bg='#FFFFCC',fg='#990000')
            Q_label2.pack()
    
            Q_button2 = tk.Button(master=window,text='แสดง',width=10,command=Td,bg='#FFCC99')
            Q_button2.pack(pady=10)
    
            Q_label3 = tk.Label(master=window,text='วันพฤหัสบอดี',bg='#FFFFCC',fg='#990000')
            Q_label3.pack()
    
            Q_button2 = tk.Button(master=window,text='แสดง',width=10,command=Trd,bg='#FFCC99')
            Q_button2.pack(pady=10)
        
            Q_output = tk.Label(master=window,bg='#FFFFCC',fg='black')
            Q_output.pack(pady=10)
    
            window.mainloop()
    
#--------------------------------------Ca------------------------------------   
        def Ca():
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
    
    
#--------------------------------------Pop------------------------------------ 
        def pop():
            window = tk.Tk()
            window.title('โปรแกรมคำนวณความน่าจะเป็น')
            window.minsize(width=600,height=600)
            window.configure(background='#FFFFCC')
    
            def Ftr1():
                def factorail(n):
        
                    f = 1
    
                    for i in range(1,n+1):
                        f = (f*i)
                    return f
    
                def Factorail1():
                    n = int(Q_input.get())
                    r = int(Q_input2.get())
                    f = int(n-r)
                    F = factorail(int(f))
                    N = factorail(int(n))
                    A = float(N/F)
                    output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                  '('+str(r)+'-'+' '+str(n)+')'+'!'+'\n'+'\n'+'   '+str(n)+'!'+
                  '\n'+'=   '+' -----------'+'\n'+'  '+str(f)+
                  '!'+'\n'+'\n'+'='+'    '+str(A)
                   )
                    Q_output.configure(text=output)
    
                def Factorail2():
                    n = int(Q_input.get())
                    r = int(Q_input2.get())
                    f = int(n-r)
                    F = factorail(int(f))
                    R = factorail(int(r))
                    N = factorail(int(n))
                    A = float(N/(R*F))
                    output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                  str(r)+'!'+' '+'('+str(n)+' '+'-'+' '+str(r)+')'+'!'+'\n'+'\n'+'   '
                  +str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'  '+str(r)+
                  '!'+' '+str(f)+'!'+'\n'+'\n'+'='+'    '+str(A)
                   )
    
                    Q_output.configure(text=output)
    
                def clear():
                    output = ' '
                    Q_output.configure(text=output)
               
    
                Q_label = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด',bg='#FFFFCC',fg='#990000')
                Q_label.place(x=30,y=0)
        
                Q_label2 = tk.Label(master=window,text='ใส่  n',bg='#FFFFCC',fg='#990000')
                Q_label2.place(x=70,y=20)
        
                Q_input = tk.Entry(master=window)
                Q_input.place(x=20,y=40)
        
                Q_label3 = tk.Label(master=window,text='ใส่  r',bg='#FFFFCC',fg='#990000')
                Q_label3.place(x=70,y=60)
    
                Q_input2 = tk.Entry(master=window)
                Q_input2.place(x=20,y=90)
    
                Q_label4 = tk.Label(master=window,text='สูตรจัดหมู่ n-r',bg='#FFFFCC',fg='#990000')
                Q_label4.place(x=10,y=130)
    
                Q_button = tk.Button(master=window,text='N-R',width=5,command=Factorail1,bg='#FFCC99')
                Q_button.place(x=20,y=160)
    
                Q_button2 = tk.Button(master=window,text='R( N-R )',width=5,command=Factorail2,bg='#FFCC99')
                Q_button2.place(x=100,y=160)
    
                Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear,bg='#FFCC99')
                Q_button5.place(x=50,y=350)
    
                Q_label5 = tk.Label(master=window,text='สูตร\nสับเปลี่ยน r(n-r)',bg='#FFFFCC',fg='#990000')
                Q_label5.place(x=80,y=120)
    
    
                Q_output = tk.Label(master=window,bg='#FFFFCC')
                Q_output.place(x=30,y=200)
            
                Q_output1 = tk.Label(master=window,bg='#FFFFCC')
                Q_output1.place(x=250,y=200)
    
                def Ftr2():
                    def Factorail3():
                        n = int(Q_input3.get())
                        r = int(Q_input4.get())
                        f = int(n-r)
                        F = factorail(int(f))
                        N = factorail(int(n))
                        A = float(N/F)
                        output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                          '('+str(r)+'-'+' '+str(n)+')'+'!'+'\n'+'\n'+'   '+str(n)+'!'+
                          '\n'+'=   '+' -----------'+'\n'+'  '+str(f)+
                          '!'+'\n'+'\n'+'='+'    '+str(A)
                       )
                        Q_output1.configure(text=output)
        
                    def Factorail4():
                        n = int(Q_input3.get())
                        r = int(Q_input4.get())
                        f = int(n-r)
                        F = factorail(int(f))
                        R = factorail(int(r))
                        N = factorail(int(n))
                        A = float(N/(R*F))
                        output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                      str(r)+'!'+' '+'('+str(n)+' '+'-'+' '+str(r)+')'+'!'+'\n'+'\n'+'   '
                      +str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'  '+str(r)+
                      '!'+' '+str(f)+'!'+'\n'+'\n'+'='+'    '+str(A)
                       )
    
                        Q_output1.configure(text=output)
    
                    def clear():
                        output = ' '
                        Q_output.configure(text=output)
                        Q_output5.configure(text=output)
    
                    def clear2():
                        output = ' '
                        Q_output1.configure(text=output)
                    
        
    
                    Q_labe6 = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด',bg='#FFFFCC',fg='#990000')
                    Q_labe6.place(x=250,y=0)
    
                    Q_label7 = tk.Label(master=window,text='ใส่  n',bg='#FFFFCC',fg='#990000')
                    Q_label7.place(x=280,y=20)
        
                    Q_input3 = tk.Entry(master=window)
                    Q_input3.place(x=230,y=40)
    
                    Q_label8 = tk.Label(master=window,text='ใส่  r',bg='#FFFFCC',fg='#990000')
                    Q_label8.place(x=280,y=60)
    
                    Q_input4 = tk.Entry(master=window)
                    Q_input4.place(x=230,y=90)
    
                    Q_label9 = tk.Label(master=window,text='สูตรจัดหมู่ n-r',bg='#FFFFCC',fg='#990000')
                    Q_label9.place(x=210,y=130)
    
                    Q_button3 = tk.Button(master=window,text='N-R',width=5,command=Factorail3,bg='#FFCC99')
                    Q_button3.place(x=220,y=160)
    
                    Q_button4 = tk.Button(master=window,text='R( N-R )',width=5,command=Factorail4,bg='#FFCC99')
                    Q_button4.place(x=320,y=160)
    
                    Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear2,bg='#FFCC99')
                    Q_button5.place(x=300,y=350)
    
                    Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear,bg='#FFCC99')
                    Q_button5.place(x=50,y=350)
    
                    Q_label10 = tk.Label(master=window,text='สูตร\nสับเปลี่ยน r(n-r)',bg='#FFFFCC',fg='#990000')
                    Q_label10.place(x=300,y=120)
    
                    Q_output1 = tk.Label(master=window,bg='#FFFFCC')
                    Q_output1.place(x=250,y=200)
    
                    def Claer():
                        output = '  '
    
                        Q_output3.configure(text=output)
                
                    Q_output3 = Label(window,width=10,height=5,bg='#FFFFCC').place(x=150,y=0)
                    def Pop1():
                        z = int(Q_input.get())
                        x = int(Q_input2.get())
                        c = int(z-x)
                        C = factorail(int(c))
                        X = factorail(int(x))
                        Z = factorail(int(z))
                        V = int(Z/(X*C))
                        n = int(Q_input3.get())
                        r = int(Q_input4.get())
                        f = int(n-r)
                        F = factorail(int(f))
                        R = factorail(int(r))
                        N = factorail(int(n))
                        A = int(N/(R*F))
                        B = float(A/V)
                        P = B*100
                        output ='ความน่าจะเป็นของ ข้อ 1\n'+'= '+'P(A)\n\n'+'n(A)\n'+'= '+'----------\n'\
                         +'n(B)\n\n'+str(V)+'\n=    '+'----------\n'+str(A)+\
                         '\n'+'=  '+'%.2f'%B+'  '+'%.f'%P+'%'
    
                        Q_output5.configure(text=output)
                
                    Q_button6 = Button(window,text='Pop ข้อ1',width=5,command=Pop1,bg='#FFCC99').place(x=50,y=390)
                    Q_output5 = Label(window,bg='#FFFFCC')
                    Q_output5.place(x=20,y=420)
    
            
                def Ftr3():
                    def Factorail5():
                        n = int(Q_input5.get())
                        r = int(Q_input6.get())
                        f = int(n-r)
                        F = factorail(int(f))
                        N = factorail(int(n))
                        A = float(N/F)
                        output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                      '('+str(r)+'-'+' '+str(n)+')'+'!'+'\n'+'\n'+'   '+str(n)+'!'+
                      '\n'+'=   '+' -----------'+'\n'+'  '+str(f)+
                      '!'+'\n'+'\n'+'='+'    '+str(A)
                       )
                        Q_output2.configure(text=output)
    
                    def Factorail6():
                        n = int(Q_input5.get())
                        r = int(Q_input6.get())
                        f = int(n-r)
                        F = factorail(int(f))
                        R = factorail(int(r))
                        N = factorail(int(n))
                        A = float(N/(R*F))
                        output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                      str(r)+'!'+' '+'('+str(n)+' '+'-'+' '+str(r)+')'+'!'+'\n'+'\n'+'   '
                      +str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'  '+str(r)+
                      '!'+' '+str(f)+'!'+'\n'+'\n'+'='+'    '+str(A)
                       )
    
                        Q_output2.configure(text=output)
    
                    def clear4():
                        output = ' '
                        Q_output6.configure(text=output)
                        Q_output8.configure(text=output)
        
                    Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear4,bg='#FFCC99')
                    Q_button5.place(x=250,y=350)
    
                    Q_output8 = tk.Label(master=window,bg='#FFFFCC')
                    Q_output8.place(x=250,y=200)
    
                    def clear3():
                        output = ' '
                        Q_output2.configure(text=output)
                        Q_output7.configure(text=output)
    
                    def Pop2():
                        z = int(Q_input.get())
                        x = int(Q_input2.get())
                        c = int(z-x)
                        C = factorail(int(c))
                        X = factorail(int(x))
                        Z = factorail(int(z))
                        V = int(Z/(X*C))
                        n = int(Q_input5.get())
                        r = int(Q_input6.get())
                        f = int(n-r)
                        F = factorail(int(f))
                        R = factorail(int(r))
                        N = factorail(int(n))
                        A = int(N/(R*F))
                        B = float(A/V)
                        P = B*100
                        output ='ความน่าจะเป็นของ ข้อ 2\n'+'= '+'P(A)\n\n'+'n(A)\n'+'= '+'----------\n'\
                         +'n(B)\n\n'+str(V)+'\n=    '+'----------\n'+str(A)+'\n'+'=  '\
                         +'%.2f'%B+'    '+'%.f'%P+'%'
    
                        Q_output6.configure(text=output)
        
                    Q_button7 = Button(window,text='Pop ข้อ2',width=5,command=Pop2,bg='#FFCC99').place(x=270,y=390)
                    Q_output6 = Label(window,bg='#FFFFCC')
                    Q_output6.place(x=250,y=420)
    
        
    
                    Q_label6 = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด',bg='#FFFFCC',fg='#990000')
                    Q_label6.place(x=450,y=0)
        
                    Q_label7 = tk.Label(master=window,text='ใส่  n',bg='#FFFFCC',fg='#990000')
                    Q_label7.place(x=480,y=20)
    
                    Q_input5 = tk.Entry(master=window)
                    Q_input5.place(x=435,y=40)
        
                    Q_label8 = tk.Label(master=window,text='ใส่  r',bg='#FFFFCC',fg='#990000')
                    Q_label8.place(x=480,y=60)
    
                    Q_input6 = tk.Entry(master=window)
                    Q_input6.place(x=435,y=90)
    
                    Q_label9 = tk.Label(master=window,text='สูตรจัดหมู่ n-r',bg='#FFFFCC',fg='#990000')
                    Q_label9.place(x=420,y=130)
    
                    Q_button3 = tk.Button(master=window,text='N-R',width=5,command=Factorail5,bg='#FFCC99')
                    Q_button3.place(x=430,y=160)
    
                    Q_button4 = tk.Button(master=window,text='R( N-R )',width=5,command=Factorail6,bg='#FFCC99')
                    Q_button4.place(x=515,y=160)
    
                    Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear3,bg='#FFCC99')
                    Q_button5.place(x=475,y=350)
    
    
                    Q_label10 = tk.Label(master=window,text='สูตร\nสับเปลี่ยน r(n-r)',bg='#FFFFCC',fg='#990000')
                    Q_label10.place(x=500,y=120)
    
    
                    Q_output2 = tk.Label(master=window,bg='#FFFFCC')
                    Q_output2.place(x=450,y=200)
    
                    def Claer2():
                        output = '  '
    
                        Q_output4.configure(text=output)
                
                    Q_output4 = Label(window,width=10,height=5,bg='#FFFFCC').place(x=350,y=0)
    
                    def Pop3():
                        n = int(Q_input7.get())
                        r = int(Q_input8.get())
                        a = n/r
                        P = a*100
                        output = 'ความน่าจะเป็นของ ข้อ 3\n'+'= '+'P(A)\n\n'+'n(A)\n'+'= '+'----------\n'\
                         +'n(B)\n\n'+str(n)+'\n=    '+'----------\n'+str(r)+'\n'+'=  '\
                         +'%.2f'%a+'    '+'%.f'%P+'%'


                        Q_output7.configure(text=output)
            
                    Q_input7 = Entry(window)
                    Q_input7.place(x=450,y=440)
                    Q_input8 = Entry(window)
                    Q_input8.place(x=450,y=460)
                    Q_button8 = Button(window,text='Pop ข้อ3',width=5,command=Pop3,bg='#FFCC99').place(x=475,y=390)
                    Q_output7 = Label(window,bg='#FFFFCC')
                    Q_output7.place(x=450,y=420)

                Button(window,text='เพิ่มเติม',width=5,command=Ftr2,bg='#FFCC99').place(x=150,y=0)
                Button(window,text='เพิ่มเติม',width=5,command=Ftr3,bg='#FFCC99').place(x=350,y=0)
                window.mainloop()
    
            if __name__ =='__main__':
                Ftr1()

#--------------------------------------ปุ่มตัวเลือก------------------------------------
        def grid():
            Button(root,text='ความน่าจะเป็น',width=10,height=2,bg='#FFCCCC',command=pop).grid(row=0,column=0)
            Button(root,text='เครื่องคิดเลข',width=10,height=2,bg='#FFCCCC',command=Ca).grid(row=1,column=0)
            Button(root,text='ตารางเรียน',width=10,height=2,bg='#FFCCCC',command=CLASS).grid(row=2,column=0)
    
            root.mainloop()

        if __name__ == '__main__':
            grid()


#############################################-PGALL-#############################        
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
        def open_txt():
            text_file = filedialog.askopenfilename(initialdir="C:/Users/Administrator.AIO-20200809NZH/AppData/Local/Programs/Python/Python39/save",title='Open Text File',filetypes=(('PY File','*.py'),))
            text_file = open(text_file,'r')
            text_file.read()

        Button(root,text='open floder',command=open_txt,bg='#FFCC99').place(x=165,y=100)
    def sh():
        w = str(et1.get())
        so = 'song'
        s = 'save'
        p = 'photo'
        b = 'book'
        sbc = 'sbc'
        cr = 'classroom'
        app = 'app'
        pgall = 'pgall'
        e = song()if w==so else save()if  w==s else photo()if w==p else book()\
            if w==b else school() if w==sbc else classroom() if w==cr else\
            app() if w==app else PGALL() if w==pgall else helps()

        op1.configure(text=e)

   

    lb1 = Label(root,text='ใส่รหัสสิ',\
      fg='#990000',font=('Tahoma',10)).pack()
    et1 = Entry(root,width=10)
    et1.pack(pady=10)
    bt1 = Button(root,text='unrlock',\
      command=sh,bg='#FFCCCC',cursor='gumby',font=('Tahoma',10))
    bt1.pack(pady=10)
    op1 = Label(root,bg='#f1d8db',\
      font=('Tahoma',12))
    op1.pack()
    mb1 = Menubutton(root,text='V',relief=RAISED,direction=RIGHT,\
      width=1,height=1,font=('Tahoma',5),bg='#FFCCCC')
    mb1.place(x=234,y=33)
    mb1.menu = Menu(mb1,tearoff=0)
    mb1['menu']=mb1.menu
    mb1.menu.add_checkbutton(label='clare',command=new)
    mb1.menu.add_checkbutton(label='clareall')
    mb1.place(x=234,y=33)


    root.mainloop()

############################################-new-#################################    
def app():
    webbrowser.open('https://www.youtube.com/watch?v=mCdaP4-DLjM')
def classroom():
    def Math():
        webbrowser.open('https://classroom.google.com/u/3/c/MzcwMjUwMTI5OTU0')
    def THAI():
        webbrowser.open('https://classroom.google.com/u/3/c/MzcwNDkxNzc3MDk4')
    def MATH():
        webbrowser.open('https://classroom.google.com/u/3/c/MzcwNjQ4NTIxNzY2')
    def TN():
        webbrowser.open('https://classroom.google.com/u/0/c/MjI2MzA5NDM4NjU4')
    def PG():
        webbrowser.open('https://classroom.google.com/u/0/c/MzcxNDY3MjIzMDY3')   
    bt1 = Button(root,text='คณิตสถิติ',command=Math,bg='#FFCC99',font=('Tahoma',10)).place(x=10,y=130)
    Button(root,text='ภาษาไทย',command=THAI,bg='#FFCC99',font=('Tahoma',10)).place(x=100,y=130)
    Button(root,text='คณิตพื้นฐาน',command=MATH,bg='#FFCC99',font=('Tahoma',10)).place(x=190,y=130)
    Button(root,text='เทคโนโลยี',command=TN,bg='#FFCC99',font=('Tahoma',10)).place(x=300,y=130)
    Button(root,text='โปรแกรม',command=MATH,bg='#FFCC99',font=('Tahoma',10)).place(x=10,y=200)   
    c = ' '
    op1.configure(text=c)
def helps():
    h = 'sbc ---> เว็ป รร.'+'\n'+'song ---> เพลง'+'\n'+'book ---> สูตรต่างๆ'+'\n'+\
        'save ---> รูปภาพ'+'\n'+'classroom ---> ชั้นเรียน'
    op1.configure(text=h)
def school():
    webbrowser.open('https://reg.southeast.ac.th/registrar/home.asp')
    c = ' '
    op1.configure(text=c)
def book():
    def alls():
        f = open(r'C:\Users\Administrator.AIO-20200809NZH\AppData\Local\Programs\Python\Python39\save\text\สูตรรวม.txt', 'r',encoding='utf-8')
        s = f.read()
        my_text.insert(END,s)
        f.close
    my_text = Text(root,width=50,height=20)
    my_text.pack(pady=20)
    def POP():
        import pop
        pop.Ftr1()
    bt2 = Button(root,text='สูตรทั้งหมด',command=alls,bg='#FFCC99')
    bt2.place(x=10,y=130)
    bt4 = Button(root,text='POP',command=POP,bg='#FFCC99')
    bt4.place(x=150,y=130)
    c = ' '
    op1.configure(text=c)
###################################PGALL###########################################
def PGALL():
    root = Tk()
    root.title('สูตรรวม')
    root.minsize(width=400,height=400)
    root.configure(background='#f1d8db')

#--------------------------------------CLASS------------------------------------
    def CLASS():
        def Md():
            output = ('คาบเช้า 9.00-12.00'+'\n'+'\n'+'166-016-408-3'+'\n'+'อาจารย์ สุณี ทิพย์เกษร'+'\n'\
                     +'\n'+'--------------------'+'\n' +'คาบบ่าย 13.00-16.00'+'\n'+'\n'+'166-077-9779'+'\n'+'อาจารย์ สุชาติ รมณียารักษ์')
            Q_output.configure(text=output)
        def Td():
            output = ('คาบเช้า 9.00-12.00'+'\n'+'\n'+'166-997-585-2'+'\n'+'อาจารย์ บริสุทธิ์ ผึ่งผดุง'+'\n'\
                 +'\n'+'--------------------'+'\n' +'คาบบ่าย 13.00-16.00'+'\n'+'\n'+'918-000-519'+'\n'+\
                  'ผู้ช่วยศาสตราจารย์ ดร.อาจารย์ รวมพร ทองรัศมี')
            Q_output.configure(text=output)
        def Trd():
            output = ('คาบเช้า 9.00-12.00'+'\n'+'\n'+'166-828-062-5'+'\n'+'อาจารย์ อภิชิต เสมศรี'+'\n'\
                 +'\n'+'--------------------'+'\n' +'คาบบ่าย 13.00-16.00'+'\n'+'\n'+'166-594-7544'+'\n'+\
              'ดร.ธีรพล ลิ้มศรัทธา')
            Q_output.configure(text=output)
    
        window = tk.Tk()
        window.title('ตารางเรียน ปี 64')
        window.minsize(width=400,height=400)
        window.configure(background='#FFFFCC')

        Q_label = tk.Label(master=window,text='วันจันทร์',bg='#FFFFCC',fg='#990000')
        Q_label.pack()

        Q_button = tk.Button(master=window,text='แสดง',width=10,command=Md,bg='#FFCC99')
        Q_button.pack(pady=10)

        Q_label2 = tk.Label(master=window,text='วันอังคาร',bg='#FFFFCC',fg='#990000')
        Q_label2.pack()

        Q_button2 = tk.Button(master=window,text='แสดง',width=10,command=Td,bg='#FFCC99')
        Q_button2.pack(pady=10)

        Q_label3 = tk.Label(master=window,text='วันพฤหัสบอดี',bg='#FFFFCC',fg='#990000')
        Q_label3.pack()

        Q_button2 = tk.Button(master=window,text='แสดง',width=10,command=Trd,bg='#FFCC99')
        Q_button2.pack(pady=10)

        Q_output = tk.Label(master=window,bg='#FFFFCC',fg='black')
        Q_output.pack(pady=10)

        window.mainloop()

#--------------------------------------Ca------------------------------------   
    def Ca():
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
    
    
    #--------------------------------------Pop------------------------------------ 
    def pop():
        window = tk.Tk()
        window.title('โปรแกรมคำนวณความน่าจะเป็น')
        window.minsize(width=600,height=600)
        window.configure(background='#FFFFCC')
    
    def Ftr1():
        def factorail(n):
        
            f = 1
    
        for i in range(1,n+1):
            f = (f*i)
        return f
    
        def Factorail1():
            n = int(Q_input.get())
            r = int(Q_input2.get())
            f = int(n-r)
            F = factorail(int(f))
            N = factorail(int(n))
            A = float(N/F)
            output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                  '('+str(r)+'-'+' '+str(n)+')'+'!'+'\n'+'\n'+'   '+str(n)+'!'+
                  '\n'+'=   '+' -----------'+'\n'+'  '+str(f)+
                  '!'+'\n'+'\n'+'='+'    '+str(A)
                   )
            Q_output.configure(text=output)
    
        def Factorail2():
            n = int(Q_input.get())
            r = int(Q_input2.get())
            f = int(n-r)
            F = factorail(int(f))
            R = factorail(int(r))
            N = factorail(int(n))
            A = float(N/(R*F))
            output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                  str(r)+'!'+' '+'('+str(n)+' '+'-'+' '+str(r)+')'+'!'+'\n'+'\n'+'   '
                  +str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'  '+str(r)+
                  '!'+' '+str(f)+'!'+'\n'+'\n'+'='+'    '+str(A)
                   )
    
            Q_output.configure(text=output)
    
        def clear():
            output = ' '
            Q_output.configure(text=output)
               
    
        Q_label = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด',bg='#FFFFCC',fg='#990000')
        Q_label.place(x=30,y=0)
        
        Q_label2 = tk.Label(master=window,text='ใส่  n',bg='#FFFFCC',fg='#990000')
        Q_label2.place(x=70,y=20)
    
        Q_input = tk.Entry(master=window)
        Q_input.place(x=20,y=40)
    
        Q_label3 = tk.Label(master=window,text='ใส่  r',bg='#FFFFCC',fg='#990000')
        Q_label3.place(x=70,y=60)
    
        Q_input2 = tk.Entry(master=window)
        Q_input2.place(x=20,y=90)
    
        Q_label4 = tk.Label(master=window,text='สูตรจัดหมู่ n-r',bg='#FFFFCC',fg='#990000')
        Q_label4.place(x=10,y=130)
    
        Q_button = tk.Button(master=window,text='N-R',width=5,command=Factorail1,bg='#FFCC99')
        Q_button.place(x=20,y=160)
    
        Q_button2 = tk.Button(master=window,text='R( N-R )',width=5,command=Factorail2,bg='#FFCC99')
        Q_button2.place(x=100,y=160)
    
        Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear,bg='#FFCC99')
        Q_button5.place(x=50,y=350)
    
        Q_label5 = tk.Label(master=window,text='สูตร\nสับเปลี่ยน r(n-r)',bg='#FFFFCC',fg='#990000')
        Q_label5.place(x=80,y=120)
    
    
        Q_output = tk.Label(master=window,bg='#FFFFCC')
        Q_output.place(x=30,y=200)
            
        Q_output1 = tk.Label(master=window,bg='#FFFFCC')
        Q_output1.place(x=250,y=200)
    
        def Ftr2():
            def Factorail3():
                n = int(Q_input3.get())
                r = int(Q_input4.get())
                f = int(n-r)
                F = factorail(int(f))
                N = factorail(int(n))
                A = float(N/F)
                output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                      '('+str(r)+'-'+' '+str(n)+')'+'!'+'\n'+'\n'+'   '+str(n)+'!'+
                      '\n'+'=   '+' -----------'+'\n'+'  '+str(f)+
                      '!'+'\n'+'\n'+'='+'    '+str(A)
                       )
                Q_output1.configure(text=output)
        
            def Factorail4():
                n = int(Q_input3.get())
                r = int(Q_input4.get())
                f = int(n-r)
                F = factorail(int(f))
                R = factorail(int(r))
                N = factorail(int(n))
                A = float(N/(R*F))
                output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                  str(r)+'!'+' '+'('+str(n)+' '+'-'+' '+str(r)+')'+'!'+'\n'+'\n'+'   '
                  +str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'  '+str(r)+
                  '!'+' '+str(f)+'!'+'\n'+'\n'+'='+'    '+str(A)
                   )
    
                Q_output1.configure(text=output)
    
            def clear():
                output = ' '
                Q_output.configure(text=output)
                Q_output5.configure(text=output)
    
            def clear2():
                output = ' '
                Q_output1.configure(text=output)
                    
        
    
            Q_labe6 = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด',bg='#FFFFCC',fg='#990000')
            Q_labe6.place(x=250,y=0)
    
            Q_label7 = tk.Label(master=window,text='ใส่  n',bg='#FFFFCC',fg='#990000')
            Q_label7.place(x=280,y=20)
        
            Q_input3 = tk.Entry(master=window)
            Q_input3.place(x=230,y=40)
    
            Q_label8 = tk.Label(master=window,text='ใส่  r',bg='#FFFFCC',fg='#990000')
            Q_label8.place(x=280,y=60)
    
            Q_input4 = tk.Entry(master=window)
            Q_input4.place(x=230,y=90)

            Q_label9 = tk.Label(master=window,text='สูตรจัดหมู่ n-r',bg='#FFFFCC',fg='#990000')
            Q_label9.place(x=210,y=130)
    
            Q_button3 = tk.Button(master=window,text='N-R',width=5,command=Factorail3,bg='#FFCC99')
            Q_button3.place(x=220,y=160)
    
            Q_button4 = tk.Button(master=window,text='R( N-R )',width=5,command=Factorail4,bg='#FFCC99')
            Q_button4.place(x=320,y=160)
    
            Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear2,bg='#FFCC99')
            Q_button5.place(x=300,y=350)
    
            Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear,bg='#FFCC99')
            Q_button5.place(x=50,y=350)
    
            Q_label10 = tk.Label(master=window,text='สูตร\nสับเปลี่ยน r(n-r)',bg='#FFFFCC',fg='#990000')
            Q_label10.place(x=300,y=120)
    
            Q_output1 = tk.Label(master=window,bg='#FFFFCC')
            Q_output1.place(x=250,y=200)

            def Claer():
                output = '  '
    
                Q_output3.configure(text=output)
                
            Q_output3 = Label(window,width=10,height=5,bg='#FFFFCC').place(x=150,y=0)
            def Pop1():
                z = int(Q_input.get())
                x = int(Q_input2.get())
                c = int(z-x)
                C = factorail(int(c))
                X = factorail(int(x))
                Z = factorail(int(z))
                V = int(Z/(X*C))
                n = int(Q_input3.get())
                r = int(Q_input4.get())
                f = int(n-r)
                F = factorail(int(f))
                R = factorail(int(r))
                N = factorail(int(n))
                A = int(N/(R*F))
                B = float(A/V)
                P = B*100
                output ='ความน่าจะเป็นของ ข้อ 1\n'+'= '+'P(A)\n\n'+'n(A)\n'+'= '+'----------\n'\
                         +'n(B)\n\n'+str(V)+'\n=    '+'----------\n'+str(A)+\
                         '\n'+'=  '+'%.2f'%B+'  '+'%.f'%P+'%'
    
                Q_output5.configure(text=output)
                
            Q_button6 = Button(window,text='Pop ข้อ1',width=5,command=Pop1,bg='#FFCC99').place(x=50,y=390)
            Q_output5 = Label(window,bg='#FFFFCC')
            Q_output5.place(x=20,y=420)
    
        
        def Ftr3():
            def Factorail5():
                n = int(Q_input5.get())
                r = int(Q_input6.get())
                f = int(n-r)
                F = factorail(int(f))
                N = factorail(int(n))
                A = float(N/F)
                output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                  '('+str(r)+'-'+' '+str(n)+')'+'!'+'\n'+'\n'+'   '+str(n)+'!'+
                  '\n'+'=   '+' -----------'+'\n'+'  '+str(f)+
                  '!'+'\n'+'\n'+'='+'    '+str(A)
                   )
                Q_output2.configure(text=output)
    
            def Factorail6():
                n = int(Q_input5.get())
                r = int(Q_input6.get())
                f = int(n-r)
                F = factorail(int(f))
                R = factorail(int(r))
                N = factorail(int(n))
                A = float(N/(R*F))
                output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
                  str(r)+'!'+' '+'('+str(n)+' '+'-'+' '+str(r)+')'+'!'+'\n'+'\n'+'   '
                  +str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'  '+str(r)+
                  '!'+' '+str(f)+'!'+'\n'+'\n'+'='+'    '+str(A)
                   )
    
                Q_output2.configure(text=output)
    
            def clear4():
                output = ' '
                Q_output6.configure(text=output)
                Q_output8.configure(text=output)
    
            Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear4,bg='#FFCC99')
            Q_button5.place(x=250,y=350)
    
            Q_output8 = tk.Label(master=window,bg='#FFFFCC')
            Q_output8.place(x=250,y=200)
    
            def clear3():
                output = ' '
                Q_output2.configure(text=output)
                Q_output7.configure(text=output)
    
            def Pop2():
                z = int(Q_input.get())
                x = int(Q_input2.get())
                c = int(z-x)
                C = factorail(int(c))
                X = factorail(int(x))
                Z = factorail(int(z))
                V = int(Z/(X*C))
                n = int(Q_input5.get())
                r = int(Q_input6.get())
                f = int(n-r)
                F = factorail(int(f))
                R = factorail(int(r))
                N = factorail(int(n))
                A = int(N/(R*F))
                B = float(A/V)
                P = B*100
                output ='ความน่าจะเป็นของ ข้อ 2\n'+'= '+'P(A)\n\n'+'n(A)\n'+'= '+'----------\n'\
                         +'n(B)\n\n'+str(V)+'\n=    '+'----------\n'+str(A)+'\n'+'=  '\
                         +'%.2f'%B+'    '+'%.f'%P+'%'
    
                Q_output6.configure(text=output)
    
            Q_button7 = Button(window,text='Pop ข้อ2',width=5,command=Pop2,bg='#FFCC99').place(x=270,y=390)
            Q_output6 = Label(window,bg='#FFFFCC')
            Q_output6.place(x=250,y=420)
    
        
    
            Q_label6 = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด',bg='#FFFFCC',fg='#990000')
            Q_label6.place(x=450,y=0)
    
            Q_label7 = tk.Label(master=window,text='ใส่  n',bg='#FFFFCC',fg='#990000')
            Q_label7.place(x=480,y=20)
    
            Q_input5 = tk.Entry(master=window)
            Q_input5.place(x=435,y=40)
    
            Q_label8 = tk.Label(master=window,text='ใส่  r',bg='#FFFFCC',fg='#990000')
            Q_label8.place(x=480,y=60)
    
            Q_input6 = tk.Entry(master=window)
            Q_input6.place(x=435,y=90)
    
            Q_label9 = tk.Label(master=window,text='สูตรจัดหมู่ n-r',bg='#FFFFCC',fg='#990000')
            Q_label9.place(x=420,y=130)
    
            Q_button3 = tk.Button(master=window,text='N-R',width=5,command=Factorail5,bg='#FFCC99')
            Q_button3.place(x=430,y=160)
    
            Q_button4 = tk.Button(master=window,text='R( N-R )',width=5,command=Factorail6,bg='#FFCC99')
            Q_button4.place(x=515,y=160)
    
            Q_button5 = tk.Button(master=window,text='Clear',width=5,command=clear3,bg='#FFCC99')
            Q_button5.place(x=475,y=350)
    
    
            Q_label10 = tk.Label(master=window,text='สูตร\nสับเปลี่ยน r(n-r)',bg='#FFFFCC',fg='#990000')
            Q_label10.place(x=500,y=120)
    
    
            Q_output2 = tk.Label(master=window,bg='#FFFFCC')
            Q_output2.place(x=450,y=200)
    
            def Claer2():
                output = '  '
    
                Q_output4.configure(text=output)
                
            Q_output4 = Label(window,width=10,height=5,bg='#FFFFCC').place(x=350,y=0)
    
            def Pop3():
                n = int(Q_input7.get())
                r = int(Q_input8.get())
                a = n/r
                P = a*100
                output = 'ความน่าจะเป็นของ ข้อ 3\n'+'= '+'P(A)\n\n'+'n(A)\n'+'= '+'----------\n'\
                         +'n(B)\n\n'+str(n)+'\n=    '+'----------\n'+str(r)+'\n'+'=  '\
                         +'%.2f'%a+'    '+'%.f'%P+'%'
    
    
                Q_output7.configure(text=output)
                
            Q_input7 = Entry(window)
            Q_input7.place(x=450,y=440)
            Q_input8 = Entry(window)
            Q_input8.place(x=450,y=460)
            Q_button8 = Button(window,text='Pop ข้อ3',width=5,command=Pop3,bg='#FFCC99').place(x=475,y=390)
            Q_output7 = Label(window,bg='#FFFFCC')
            Q_output7.place(x=450,y=420)
    
            Button(window,text='เพิ่มเติม',width=5,command=Ftr2,bg='#FFCC99').place(x=150,y=0)
            Button(window,text='เพิ่มเติม',width=5,command=Ftr3,bg='#FFCC99').place(x=350,y=0)
            window.mainloop()
        
    if __name__ =='__main__':
        Ftr1()
    
#--------------------------------------ปุ่มตัวเลือก------------------------------------
    def grid():
        Button(root,text='ความน่าจะเป็น',width=10,height=2,bg='#FFCCCC',command=pop).grid(row=0,column=0)
        Button(root,text='เครื่องคิดเลข',width=10,height=2,bg='#FFCCCC',command=Ca).grid(row=1,column=0)
        Button(root,text='ตารางเรียน',width=10,height=2,bg='#FFCCCC',command=CLASS).grid(row=2,column=0)
        
        root.mainloop()
    
    if __name__ == '__main__':
        grid()
    
    
       
    
    c = ' '
    op1.configure(text=c)
####################################-PGALL#####################################   
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
    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/Users/Administrator.AIO-20200809NZH/AppData/Local/Programs/Python/Python39/save",title='Open Text File',filetypes=(('PY File','*.py'),))
        text_file = open(text_file,'r')
        text_file.read()

    Button(root,text='open floder',command=open_txt,bg='#FFCC99').place(x=165,y=100)
def sh():
    w = str(et1.get())
    so = 'song'
    s = 'save'
    p = 'photo'
    b = 'book'
    sbc = 'sbc'
    cr = 'classroom'
    app = 'app'
    pgall = 'pgall'
    e = song()if w==so else save()if  w==s else photo()if w==p else book() \
        if w==b else school() if w==sbc else classroom() if w==cr else app() \
        if w==app else PGALL() if w==pgall else helps()
    
    op1.configure(text=e)

   

lb1 = Label(root,text='ใส่รหัสสิ',\
      fg='#990000',font=('Tahoma',10)).pack()
et1 = Entry(root,width=10)
et1.pack(pady=10)
bt1 = Button(root,text='unrlock',\
      command=sh,bg='#FFCCCC',cursor='gumby',font=('Tahoma',10))
bt1.pack(pady=10)
op1 = Label(root,bg='#f1d8db',\
      font=('Tahoma',12))
op1.pack()
mb1 = Menubutton(root,text='V',relief=RAISED,direction=RIGHT,\
      width=1,height=1,font=('Tahoma',5),bg='#FFCCCC')
mb1.place(x=234,y=33)
mb1.menu = Menu(mb1,tearoff=0)
mb1['menu']=mb1.menu
mb1.menu.add_checkbutton(label='clare',command=new)
mb1.menu.add_checkbutton(label='clareall')
mb1.place(x=234,y=33)


root.mainloop()
