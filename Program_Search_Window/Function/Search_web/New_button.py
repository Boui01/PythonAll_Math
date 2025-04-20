from tkinter import *
import tkinter as tk
from tkinter import *
from tkinter import TclError, ttk
from tkinter.messagebox import  showinfo
from Function.Search_web.Search_update import Sh_web_update
from Tkinter_custom.tkinter_custom import tkinter_custom
import subprocess
import sys
import re

result = ''
class New_btn():

    def __init__(self,root ,text_check = [] , type  = ''):
        self.root2 = tk.Tk()
        self.root2.title('ADD NEW BUTTON')
        self.root2.minsize(width=400,height=50)
        self.root2.resizable(0, 0)
        self.root2.configure(background='#fae5fa')

        self.root = root
        self.tk_custom = tkinter_custom(self.root2 , bg='#FFCC99' , fg = '#ad5900')
        self.text_check = text_check

        self.Nw_label_1 = self.tk_custom.__label__(text='Name Button',bg='#fae5fa',fg='#990000')
        self.Nw_label_1.pack(side='top',fill='both',padx=50,pady=5)

        self.Nw_bar_1 = self.tk_custom.__input__(ver=2,width=18)
        self.Nw_bar_1.pack(side='top',fill='both',padx=50,pady=5)

        self.Nw_label_2 = self.tk_custom.__label__(text='Class Name',bg='#fae5fa',fg='#990000')
        self.Nw_label_2.pack(side='top',fill='both',padx=50,pady=5)

        self.Nw_bar_2 = self.tk_custom.__input__(ver=2,width=18)
        self.Nw_bar_2.pack(side='top',fill='both',padx=50,pady=5)
        
        self.Nw_label_3 = self.tk_custom.__label__(text='Web',bg='#fae5fa',fg='#990000')
        self.Nw_label_3.pack(side='top',fill='both',padx=50,pady=5)

        self.Nw_bar_3 = self.tk_custom.__input__(ver=2,width=18)
        self.Nw_bar_3.pack(side='top',fill='both',padx=50,pady=5)

        self.Label_result = self.tk_custom.__label__(text='Status Result',bg='#FBF3CD',fg='#990000')
        self.Label_result.pack(side='bottom',fill='both',padx=50,pady=15)

                            
        #-------------------------------------------------- Button --------------------------------------------------
        if type == 'Button':
            self.Nw_button_submit = self.tk_custom.__btn__(text='Submit',font=('Tahoma',8),width=5,height=1,command=lambda:self.Submit(Type = 'Button'),bg='#FAB83C')
            self.Nw_button_submit.pack(side='top',fill='both',padx=50,pady=15)

        #----------------------------------------------------- Menu  --------------------------------------------------
        elif type == 'Menu':
            self.root2.minsize(width=400,height=500)

            self.block_main = self.tk_custom.__label__( bg='#fae5fa')
            self.block_main.pack(side='top',pady=5)

            #------------------------------------------------- Block 1 --------------------------------------------------
            self.block = self.tk_custom.__label__(bg='#fae5fa')
            self.block.pack(side='left' ,in_=self.block_main)

            self.Nw_label_4 = self.tk_custom.__label__(text='Menu Name',bg='#fae5fa',fg='#990000')
            self.Nw_label_4.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)

            self.Nw_bar_4 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_4.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)

            self.Nw_label_5 = self.tk_custom.__label__(text='Web',bg='#fae5fa',fg='#990000')
            self.Nw_label_5.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)

            self.Nw_bar_5 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_5.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)

            self.Nw_label_6 = self.tk_custom.__label__(text='Menu Name 2',bg='#fae5fa',fg='#990000')
            self.Nw_label_6.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)

            self.Nw_bar_6 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_6.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)

            self.Nw_label_7 = self.tk_custom.__label__(text='Web 2',bg='#fae5fa',fg='#990000')
            self.Nw_label_7.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)

            self.Nw_bar_7 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_7.pack(side='top',fill='both',padx=50,pady=5,in_=self.block)


            #--------------------------------------------------self.Block 2 --------------------------------------------------
            self.block_2 = self.tk_custom.__label__( bg='#fae5fa')
            self.block_2.pack(side='right' ,in_=self.block_main)

            self.Nw_label_8 = self.tk_custom.__label__(text='Menu Name 3',bg='#fae5fa',fg='#990000')
            self.Nw_label_8.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_bar_8 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_8.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_label_9 = self.tk_custom.__label__(text='Web 3',bg='#fae5fa',fg='#990000')
            self.Nw_label_9.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_bar_9 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_9.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_label_10 = self.tk_custom.__label__(text='Menu Name 4',bg='#fae5fa',fg='#990000')
            self.Nw_label_10.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_bar_10 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_10.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_label_11 = self.tk_custom.__label__(text='Web 4',bg='#fae5fa',fg='#990000')
            self.Nw_label_11.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_bar_11 = self.tk_custom.__input__(ver=2,width=18)
            self.Nw_bar_11.pack(side='top',fill='both',padx=50,pady=5,in_=self.block_2)

            self.Nw_button_submit = self.tk_custom.__btn__(text='Submit',font=('Tahoma',8),width=10,height=1,command=lambda:self.Submit(Type='Menu'),bg='#FAB83C')
            self.Nw_button_submit.pack(side='bottom',fill='both',padx=50,pady=15)
    def Submit( self,Type = ''):
        result = 'Passed'
        web_class = [ self.Nw_bar_2.get() ] if Type == 'Button' else [ self.Nw_bar_2.get() , self.Nw_bar_5.get()  , self.Nw_bar_7.get()  , self.Nw_bar_9.get()  , self.Nw_bar_1.get()  ]
        pattern = re.compile(r'^\w+$')
        #----------------------------------- Validation ---------------------------------------------
        for i in web_class:
            if not re.match(pattern, i):
                result = 'Fail this web class name not correct pattern!'
                break
        for i in self.text_check:
            if Type == 'Button' and (    i == self.Nw_bar_1.get() or i == self.Nw_bar_2.get() or i == self.Nw_bar_3.get()  ):
                result  = 'Fail this name is exist!'
                break
            elif Type == 'Menu' and (   i == self.Nw_bar_1.get() or i == self.Nw_bar_2.get() or i == self.Nw_bar_3.get() or   
                                        i == self.Nw_bar_10.get() or i == self.Nw_bar_8.get() or i == self.Nw_bar_6.get() or i == self.Nw_bar_4.get()  or
                                        i == self.Nw_bar_11.get() or i == self.Nw_bar_9.get() or i == self.Nw_bar_7.get() or i == self.Nw_bar_5.get()
                                    ) :
                result  = 'Fail this name is exist!'
                break
        #----------------------------------- Make button ---------------------------------------------        
        if result == 'Passed':        
            if Type == 'Button' : 
                result = Sh_web_update(  type = Type ,
                                text = [ self.Nw_bar_1.get(),self.Nw_bar_2.get(),self.Nw_bar_3.get()]
                        ) 
                
            elif Type == 'Menu' : 
                result =  Sh_web_update(  type = Type ,
                                text = [ self.Nw_bar_1.get(),self.Nw_bar_2.get(),self.Nw_bar_3.get() ] ,
                                text_menu = [ self.Nw_bar_10.get(),self.Nw_bar_8.get(),self.Nw_bar_6.get(),self.Nw_bar_4.get() ] ,
                                text_menu_web = [ self.Nw_bar_11.get(),self.Nw_bar_9.get(),self.Nw_bar_7.get(),self.Nw_bar_5.get() ]
                        )               
            
            if(str(result) == 'Success'):
                Refresh_button = self.tk_custom.__btn__(text='Refresh',font=('Tahoma',8),width=5,height=1,command=lambda:(
                        showinfo(
                            title='Refresh',
                            message='This is refresh program for show new button.',
                        )
                        ,self.root.destroy(),self.root2.destroy(),subprocess.run([sys.executable] + sys.argv)
                    ),bg='#b8f2ed')
                Refresh_button.pack(side='bottom',fill='both',padx=50,pady=15)

        self.Label_result.config(text=str(result))   

        self.root2.mainloop()
