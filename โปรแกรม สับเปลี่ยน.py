import tkinter as tk
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
    A = int(N/F)
    output = ('   '+str(n)+'!'+'\n'+'=   '+' -----------'+'\n'+'       '+
              '('+str(r)+'-'+' '+str(n)+')'+'!'+'\n'+'\n'+'   '+str(n)+'!'+
              '\n'+'=   '+' -----------'+'\n'+'  '+str(f)+
              '!'+'\n'+'\n'+'='+'    '+str(A)
               )
    Q_output.configure(text=output)
    
window = tk.Tk()
window.title('Hen')
window.minsize(width=400,height=400)

Q_label = tk.Label(master=window,text='ใส่เลขจำนวนทั้้งหมด')
Q_label.pack()

Q_label2 = tk.Label(master=window,text='ใส่  n')
Q_label2.pack()

Q_input = tk.Entry(master=window)
Q_input.pack(pady=10)

Q_label3 = tk.Label(master=window,text='ใส่  r')
Q_label3.pack()

Q_input2 = tk.Entry(master=window)
Q_input2.pack(pady=10)

Q_button = tk.Button(master=window,text='Enter',width=10,command=Factorail1)
Q_button.pack(pady=10)

Q_output = tk.Label(master=window)
Q_output.pack(pady=10)

