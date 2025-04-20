from tkinter import *
import tkinter as tk
from Function.Web.Web import * 
from Function.Search_web.New_button import *
from Function.Search_web.Search_delete import *
from Tkinter_custom.tkinter_custom import tkinter_custom
import webbrowser


#--------------------------------------CLASS------------------------------------

class Sh_web_test: 

    def __init__(self , root , status):
        self.root = root
        self.status = status
        self.tk_custom = tkinter_custom(root , bg='#FFCC99' ,fg='#232323')

        self.list_create_btn_sh_body = [

            #-----------------------------------New_button-----------------------------------------------------
            # -------------------------- (  text , command , type / sub_mn_text , sub_mn command ) ------------
            {'text' : 'SBU Web' , 'command' : web.sbu , 'type' : 'Button' },
            {'text' : 'Cisco Web' , 'command' : web.Cisco , 'type' : 'Button' },
            {'text' : 'Theerapol Web' , 'command' : web.Theerapol , 'type' : 'Menu' , 'sub_mn_text' : ['Laravel' , 'Agular' ] , 'sub_mn_command' : [ web.Theerapol_lararel , web.Theerapol_agular]},
        ]

        self.list_btn_sh_main = []
        self.list_btn_sh_body = []
        self.list_label_sh = []
        self.list_bar_sh = []

        self.Sh_btn_head()
        self.Sh_btn_body()
        self.Sh_btn_position()

#--------------------------------------Function----------------------------------------------------
    def Back(self):
        #Back_button.place_forget()
        for i in self.list_btn_sh_main:
            i.place_forget()
            i.pack_forget()
            i.grid_forget()
        for i in self.list_btn_sh_body:
            i.place_forget()
            i.pack_forget()
            i.grid_forget()
        for i in self.list_bar_sh:
            i.place_forget()
            i.pack_forget()
            i.grid_forget()
        for i in self.list_label_sh:
            i.place_forget()
            i.pack_forget()
            i.grid_forget()            


        self.status( status='show')

        


    def Sh_btn_head(self):
    #---------------------------------Sh_web-label------------------------------------------------------------
        self.Search_label = self.tk_custom.__label__(text='Search',fg='#d9a000',font=('Tahoma',18))
        self.Search_label.grid(column=1, row=0, sticky=tk.E,padx=5 , pady=0)

        self.Main_center_label = self.tk_custom.__label__(text='Book Web',bg='',fg='#990000',font=('Tahoma',9,'bold'))
        self.Main_center_label.grid(column=2, row=1, sticky=tk.N,padx=5, pady=5)
        


    #-------------------------------------Sh_web-searh-button---------------------------------------------------------------
        self.Sh_bar = self.tk_custom.__input__(ver= 2 , width=25)
        self.Sh_bar.grid(column=2, row=0, sticky=tk.W,padx=5, pady=18)

        
        self.Sh_button = self.tk_custom.__btn__(ver=2,text='Go',width=5,command=self.Search)
        self.Sh_button.grid(column=3, row=0, sticky=tk.W, padx=1, pady=10)


        self.Nw_button = self.tk_custom.__menu__( text='New',width=4,height='small',act='',bg='#ffffff',fg='#d9a000',font=('Tahoma',8),command=lambda:New_btn( root=self.root , text_check =  map(lambda x: x.get('text') , self.list_create_btn_sh_body) , type = 'Button'),
                                        font_mn=('Tahoma',8),bg_mn='#ffd450',
                                        sub_mn_position=RIGHT,sub_mn_text=['Menu','Delete'],
                                        sub_mn_command=[lambda:New_btn( root=self.root   , text_check =  map(lambda x: x.get('text') , self.list_create_btn_sh_body) , type = 'Menu') , lambda:Sh_web_delete( root=self.root  , list_btn= self.list_create_btn_sh_body)])
        self.Nw_button.grid(column=4, row=0, sticky=tk.W, padx=10, pady=10)


    #-------------------------------------Sh_web--back-button---------------------------------------------------------------
        self.Back_button = self.tk_custom.__btn__(text='Back',width=7,font=('Tahoma',9),height='small',command=self.Back,bg='#FF7D2E')
        self.Back_button.place(x=30,y= 350)

    #------------------ Add to list ------------------------
        self.list_label_sh.append(self.Search_label)
        self.list_label_sh.append(self.Main_center_label)
        self.list_bar_sh.append(self.Sh_bar)
        self.list_btn_sh_main.append(self.Sh_button)
        self.list_btn_sh_main.append(self.Nw_button)
        self.list_btn_sh_main.append(self.Back_button)

    #-----------------------------------Function-searh-web---------------------------------------------------------------
    def Search(self):
        self.Sh_input = str('http:'+ self.Sh_bar.get())
        webbrowser.open(url= self.Sh_input)



    #-----------------------------------Sh_web-body_button---------------------------------------------------------------
    def Sh_btn_body(self):
        for i in self.list_create_btn_sh_body:
            if i['type'] == 'Button':
                button =  self.tk_custom.__btn__(text=i['text'],width=10,height='small',command=i['command'],font=('Arial',9))
            elif i['type'] == 'Menu':
                button =  self.tk_custom.__menu__(  text = i['text'] , font = ('Arial',9) , width = 12 , height = 'small', fg = '#232323', command = i['command'],
                                                font_mn= ('Arial',10),bg_mn= '#FDA069', fg_mn = '#232323',
                                                sub_mn_position = RIGHT, sub_mn_text = i['sub_mn_text'] , sub_mn_command = i['sub_mn_command'], sub_mn_bg = '' , sub_mn_fg = '')
            
            self.list_btn_sh_body.append(button)

    #-----------------------------------Sh_web-position---------------------------------------------------------------   
    def Sh_btn_position(self):
        #---------------------------------Sh_size----------------------------------------------------------------
        IntY_bottonDF = 42
        IntY_botton = IntY_bottonDF-2

        IntY_head = 50
        IntY_body = 5
        IntY_footer = 0

        x = 50
        y = (IntY_bottonDF+IntY_head+IntY_body)-IntY_footer
        numberY = 1
        numberX = 1

        for i in self.list_btn_sh_body:
            if y > 300 and numberX < 3:
                x += 120 
                y = (IntY_bottonDF+IntY_head+IntY_body)-IntY_footer
                numberY = 1
                numberX += 1

            numberY += 1                 
            i.place(x=x,y= y)
            y = (IntY_botton*numberY+IntY_head+IntY_body)-IntY_footer
    


if __name__ == '__main__':
    Sh_web_test()

