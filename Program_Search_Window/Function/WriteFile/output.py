from tkinter import *
import tkinter as tk
root = Tk()
root.title('All PROGRAM')
root.minsize(width=400,height=400)
root.configure(background='#fae5fa')

#-------Test
print(f"Found")
Sh_button = tk.Button(master=root,text='Go',font=('Tahoma',8),width=2,height=1,bg='#FAB83C')
Sh_button.place(x=320,y= -32)


root.mainloop()