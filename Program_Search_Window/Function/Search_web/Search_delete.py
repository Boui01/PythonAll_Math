import subprocess
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Tkinter_custom.tkinter_custom import tkinter_custom
from tkinter.messagebox import  showinfo
from Function.WriteFile.WriteFile import WriteFile

class Sh_web_delete:
    def __init__(self, root ,list_btn = []):
        self.root = root
        self.root2 = tk.Tk()
        self.root2.title('Replace')
        self.root2.geometry("240x200")
        self.root2.resizable(0, 0)
        self.root2.configure(background='#fae5fa')
        # layout on the self.root2 window
        self.root2.columnconfigure(0, weight=1)
        self.root2.columnconfigure(1, weight=3)
        self.root2.columnconfigure(2, weight=1)

        self.list_btn = list_btn

        self.WriteFile = WriteFile( from_file='Search_web' )
        self.tk_custom = tkinter_custom(self.root2 , bg='#FFCC99' , fg = '#ad5900')

        self.label_input = self.tk_custom.__label__(text='Please select a button:',width=20,bg='#fae5fa',fg='#990000',font=('sans-serif',10))
        self.label_input.grid(column=1, row=0 , sticky=S , pady=5)

        self.btn_cb = self.tk_custom.__select__( list_btn = map(lambda x: x['text'] , self.list_btn) , width = 15 , bg='#fae5fa',fg='#990000',font=('sans-serif',10) )
        self.btn_cb.grid(column=1, row=1 , sticky=NS , pady=5)
                

        self.delete_button = self.tk_custom.__btn__(ver=2, text='Delete' ,command=lambda:self.Delete() , width=10 )
        self.delete_button.grid(column=1, row=2 , sticky=NS , pady=5)
            
        self.result_label = self.tk_custom.__label__(text = 'Result status' , bg='#ffefd5',fg='#990000',font=('palatino',8))
        self.result_label.grid(column=1, row=3 , sticky=NS , pady=5)

        


    def Delete (self):
        status_delete = False

        for btn in self.list_btn :
            if btn['text'] == self.btn_cb.get() :
                
                if btn['type'] == 'Button' :
                    status_delete = self.WriteFile.Delete(  file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Search_web\Search_web.py' ,
                            word="" ,
                            word_find = btn['text'],
                    )
                elif btn['type'] == 'Menu' : 
                    status_delete = self.WriteFile.Delete(  file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Search_web\Search_web.py' ,
                            word="" ,
                            word_find = btn['text'],
                    )
                    for j in range(len(btn['sub_mn_command'])) :
                        status_delete = self.WriteFile.Delete(  file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Web\Web.py' ,
                                word="web_menu" ,
                                word_find = 'def '+btn['sub_mn_command'][j],
                        )
                status_delete = self.WriteFile.Delete(  file_path= r'E:\Backup_MyPC\Code\save\Pytron\Program_Search_Window\Function\Web\Web.py' ,
                        word="web" ,
                        word_find = 'def '+btn['text'],
                )

        self.result_label.config( text= status_delete )

        if status_delete == 'Success' :
            self.Refesh()

    def Refesh (self):
        Refresh_button = self.tk_custom.__btn__(text='Refresh',font=('Tahoma',8),width=8,height=1,command=lambda:(
                showinfo(
                    title='Refresh',
                    message='This is refresh program for show new button.',
                )
                ,self.root.destroy(),self.root2.destroy(),subprocess.run([sys.executable] + sys.argv)
            ),bg='#b8f2ed')
        Refresh_button.grid(column=1, row=4 , sticky=NS , pady=5)



        



Sh_delete = Sh_web_delete

if __name__ == "__main__":
    Sh_delete
