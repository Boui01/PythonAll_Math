from tkinter import *
import tkinter as tk
from tkinter import ttk
from Tkinter_custom.tkinter_custom import tkinter_custom
from Function.Search_web.Search_web import Sh_web_test
from Function.Translate_type.Translate import Translate
from Function.AI.AI import AI
from Function.Bot.Bot import Bot


root = Tk()


#----------Image------------------
#canvas = Canvas(root,width=500,height=500)
#canvas.place(x=-100,y=-80)
#pt = PhotoImage(file=r'')
#canvas.create_image(300,300,image=pt,anchor=CENTER)

#---Pt = Prosition ตำแหน่ง------
#---Sh = Shearch ค้นหาเว็บ-------- 
#root.attributes('-toolwindow', True) # Delete Icon window and tool bar top
#--------------------------------------CLASS------------------------------------
# layout on the root window
class Pg_all:

    def __init__(self):
        self.tk_custom = tkinter_custom(root , bg='#FFCC99' , fg = '#ad5900')
        self.list_btn_main = []

        #--------------------- List Btn ---------------------------
        # ------------ ( id , text , command ) ------------
        self.list_create_btn_main = [ 
            { 'id' : 1 , 'text' : 'Open Web' , 'command' : lambda: (Sh_web_test(root=root , status = self.Pg_position_btn ),self.Pg_position_btn(status = 'hide')) } ,
            { 'id' : 2 , 'text' : 'Translate file' , 'command' : lambda:(Translate(root = root , status = self.Pg_position_btn ),self.Pg_position_btn( status = 'hide')) } , 
            { 'id' : 3 , 'text' : 'AI' , 'command' : lambda: (AI(root = root , status = self.Pg_position_btn),self.Pg_position_btn( status = 'hide' )) }  ,
            { 'id' : 4 , 'text' : 'Bot' , 'command' : lambda: (Bot(root = root , status = self.Pg_position_btn),self.Pg_position_btn( status = 'hide' )) }         
        ]

    def Pg_main_btn(self):
        #--------------------- Create Btn ---------------------------
        for i in self.list_create_btn_main :
            _btn_ =  self.tk_custom.__btn__(text = i.get('text') , font = 10 , width = 'normal' , height ='small'  , command = i.get('command'))
            self.list_btn_main.append(_btn_)


        #--------------------- Update Btn ---------------------------
        self.Pg_position_btn( status = 'show')

    def Pg_position_btn(self  , status = ''):
        ct_row = 0
        ct_col = 0
        #--------------------- Position Btn ---------------------------
        if status == 'show':
            root.title('All PROGRAM')
            root.minsize(width=400,height=400)
            root.resizable(0, 0)
            root.configure(background='#ffefd5')
            root.columnconfigure(0, weight=1)
            root.columnconfigure(5, weight=1)
            
            for btn in self.list_btn_main:
                if ct_row < 4:
                    btn.grid(row = ct_row , column = ct_col , padx = 5 , pady = 20)
                    ct_row += 1
                else :
                    ct_row = 0
                    ct_col += 1
                    btn.grid(row = ct_row , column = ct_col , padx = 5 , pady = 20)
        elif status == 'hide':
            for btn in self.list_btn_main:
                btn.grid_remove()
    



# ---------------------------------------Main--------------------------------------------------------------------------
main = Pg_all()
main.Pg_main_btn()
root.mainloop()

if __name__ == '__main__':
    Pg_all()


