import tkinter as tk
def Qurtai():
    Q1 = int(Q_input.get())
    Q7 = int(Q_input6.get())
    output = ('Q'+'='+str(Q1)+'+1'+'\n'+'      ----'
              '\n'+'    4'+'\n'+'='+str((Q1+1)/Q7)
              )
    
    Q_output.configure(text=output)

def Qurtai3():
    Q6 = int(Q_input5.get())
    Q1 = int(Q_input.get())
    Q7 = int(Q_input6.get())
    output3 = ('Q'+str(Q6)+'='+str(Q6)+'('+str(Q1)+'+1'+')'+'\n'+'      ----'
              '\n'+'    4'+'\n'+'='+str(Q6*((Q1+1)/Q7))
              )
    
    Q_output.configure(text=output3)
def Qurtai4():
     Q2 = int(Q_input2.get())
     Q3 = float(Q_input3.get())
     Q4 = float(Q_input4.get())
     Q5 = float(Q4-Q2)
     Q6 = int(Q_input5.get())
     output2 = ('Q'+str(Q6)+'='+str(Q2)+'('+str(Q3)+'x'+str(Q5)+')'
                +'\n'+'='+str(Q2)+'+'+str(Q3*Q5)
                +'\n'+'='+str(Q2+(Q3*Q5))
                )

     Q_output.configure(text=output2)

def Qurtai2():
     Q2 = int(Q_input2.get())
     Q3 = float(Q_input3.get())
     Q4 = float(Q_input4.get())
     Q5 = float(Q4-Q2)
     output2 = ('Q1'+'='+str(Q2)+'('+str(Q3)+'x'+str(Q5)+')'
                +'\n'+'='+str(Q2)+'+'+str(Q3*Q5)
                +'\n'+'='+str(Q2+(Q3*Q5))
                )

     Q_output.configure(text=output2)

window = tk.Tk()
window.title('Hen')
window.minsize(width=400,height=400)

Q_label = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด')
Q_label.pack()

Q_input = tk.Entry(master=window)
Q_input.pack(pady=10)

Q_label = tk.Label(master=window,text='ใส่เศษส่วน')
Q_label.pack()

Q_input6 = tk.Entry(master=window)
Q_input6.pack(pady=10)

Q_button = tk.Button(master=window,text='Enter',width=10,command=Qurtai)
Q_button.pack(pady=10)

Q_label = tk.Label(master=window,text='ใส่เลขคอว์ไทล์มี r')
Q_label.pack()

Q_input5 = tk.Entry(master=window)
Q_input5.pack(pady=10)

Q_button3 = tk.Button(master=window,text='Enter',width=10,command=Qurtai3)
Q_button3.pack(pady=10)

Q_output = tk.Label(master=window)
Q_output.pack(pady=10)

Q_label2 = tk.Label(master=window,text='ใส่เลขตำแหน่ง')
Q_label2.pack()

Q_input2 = tk.Entry(master=window)
Q_input2.pack(pady=10)

Q_label3 = tk.Label(master=window,text='ใส่เลขทศนิยม')
Q_label3.pack()

Q_input3 = tk.Entry(master=window)
Q_input3.pack(pady=2)

Q_label4 = tk.Label(master=window,text='ใส่เลขตำแหน่งถัดไป')
Q_label4.pack()

Q_input4 = tk.Entry(master=window)
Q_input4.pack(pady=2)

Q_button2 = tk.Button(master=window,text='Enter',width=10,command=Qurtai2)
Q_button2.pack(pady=10)

Q_label2 = tk.Label(master=window,text='กดแบบคำนวณมี r')
Q_label2.pack()

Q_button2 = tk.Button(master=window,text='Enter',width=10,command=Qurtai4)
Q_button2.pack(pady=10)


Q_output2 = tk.Label(master=window)
Q_output2.pack(pady=10)

window.mainloop()
