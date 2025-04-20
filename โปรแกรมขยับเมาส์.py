import tkinter as tk
import pyautogui as pg
import time


window = tk.Tk()
window.title('ควบคุมเมาส์')
window.minsize(width=400,height=400)

tt_label = tk.Label(master=window,text='mouse')
tt_label.pack()


def Discord ():
    discord = pg.click(348,270)
    move = pg.moveTo(261,899,duration=2)
    time.sleep(1)
    google = pg.click(257,891)
    time.sleep(2)
    google1 = pg.click(630,493)

et_button = tk.Button(master=window,text='Enter',command=Discord) 
et_button.pack()

output_output = tk.Label(master=window)
output_output.pack()


window.mainloop()


