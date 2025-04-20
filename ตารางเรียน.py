from tkinter import *
import tkinter as tk

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
