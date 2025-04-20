from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import  showerror
from tkinter import filedialog as fd


class tkinter_custom:

    def __init__( self , tk , ver = 1 , font ='' , font_size ='' , width_sm ='' , width_nor ='' , width_lar ='' , height_sm ='' , height_nor ='' , height_lar ='',
                  bg ='' , fg ='' , atc ='' , bd_w = '' , bd_stlye = ''):

        self.root = tk
        self.ver = ver
        #----------------- font ------------------
        self.font_default =  'Helvetica' if font == '' else font
        self.font_default_size = 9 if font_size == '' else int(font_size)

        #----------- width and height ------------
        self.width_small = 5 if width_sm == '' else int(width_sm)
        self.width_normal = 10 if width_nor == '' else int(width_nor)
        self.width_large = 20 if width_lar == '' else int(width_lar)

        self.height_small = 1 if height_sm == '' else int(height_sm)        
        self.height_normal = 2 if height_nor == '' else int(height_nor)
        self.height_large = 3 if height_lar == '' else int(height_lar)

        #----------------- color ------------------
        self.bg_color_default = '#ffffff' if bg == '' else bg
        self.fg_color_default = '#d9a000' if fg == '' else fg
        self.atc_color_default = '#b2e0ef' if atc == '' else atc

        #----------------- box --------------------


        #----------------- border ------------------
        self.border_width_default = 1 if bd_w == '' else int(bd_w)
        self.relief_default = 'flat' if bd_stlye == '' else bd_stlye

    def __hide__(self , delete = []):
        for i in delete :
            if i in self.root.winfo_children():
                i.destroy()
            elif i in self.root.pack_slaves():
                i.pack_forget() 
            elif i in self.root.grid_slaves():
                i.grid_remove()
        
    #------------------------------------------ Button ------------------------------------------
    def __btn__(self , text ,ver = '', font ='' , width ='' , height ='',act ='', bg ='' , fg ='', cs='' , command ='' , state = ''):
        button = ''
 
        if ver == 1 or ver == '' and self.ver == 1:
            button = tk.Button(    master= self.root ,
                                    text = text ,
                                    font = (self.font_default , self.font_default_size) if font == '' else (self.font_default , int(font))  if isinstance(font, int) else (self.font_default,int(font[0]),'bold') if font[1] == 'bold' else font ,
                                    width = self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,   
                                    height =  self.height_normal if height == '' or height == 'normal' else self.height_small if height == 'small'  else  self.height_large if height == 'large' else height ,
                                    activebackground= self.atc_color_default if act == '' else act ,
                                    bg = self.bg_color_default if bg == '' else bg ,
                                    fg = self.fg_color_default if fg == '' else fg , 
                                    cursor= cs if cs != '' else 'hand2',
                                    state= tk.DISABLED if state == 'disable' else tk.NORMAL,
                                    command = command
                        )
        elif ver == 2   or ver == '' and self.ver == 2:
            button = ttk.Button(    master= self.root ,
                                    text = text ,
                                    width = self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,   
                                    cursor= cs if cs != '' else 'hand2',
                                    state= tk.DISABLED if state == 'disable' else tk.NORMAL,
                                    command = command
            )
            return button
        
        button.bind("<Enter>", lambda event: button.config(bg= self.atc_color_default if act == '' else act))
        button.bind("<Leave>", lambda event: button.config(bg=self.bg_color_default if bg == '' else bg))
        button.bind('<<ComboboxSelected>>', 'dot')
        return button
    
    #-------------------------------------------- Menu ------------------------------------------
    def __menu__(   self  , text , font ='' , width ='' , height ='',act ='', bg ='' , fg ='' , command ='' ,
                    font_mn ='' , bg_mn ='' , fg_mn ='' , 
                    sub_mn_position = RIGHT, sub_mn_text = [] , sub_mn_command = [], sub_mn_bg = '', sub_mn_fg = ''
                ):
        
        block = ttk.Label(self.root, background=self.root.cget("bg"))
        btn_menu = self.__btn__(text = text , font = font , width = width , height = height,act = act, bg = bg , fg = fg , command = command)
        menu = Menubutton ( master= self.root ,
                    text = 'v',
                    width = 0,   
                    height =  self.height_normal if height == '' or height == 'normal' else self.height_small if height == 'small'  else  self.height_large if height == 'large' else height ,
                    font = (self.font_default , self.font_default_size+1) if font_mn == '' else (self.font_default , int(font_mn))  if isinstance(font_mn, int) else (self.font_default,int(font_mn[0]),'bold') if font_mn[1] == 'bold' else font_mn ,
                    relief= RAISED,
                    direction= sub_mn_position,
                    activebackground= self.atc_color_default if act == '' else act ,
                    bg = self.bg_color_default if bg_mn == '' else bg_mn ,     
                    fg = self.fg_color_default if fg_mn == '' else fg_mn     
                )
        menu.menu  =  Menu ( menu,tearoff = 0 )
        menu["menu"]  =  menu.menu

        btn_menu.grid(row = 0 , column = 0 , sticky = 'ew' , in_ = block)
        menu.grid(row = 0 , column = 1 , sticky = 'ew' , in_ = block)
        if len(sub_mn_text) == len(sub_mn_command):
            for i in range(len(sub_mn_text)):
                menu.menu.add_command ( 
                        label = sub_mn_text[i],
                        command= sub_mn_command[i],
                        activebackground= self.atc_color_default if act == '' else act ,
                        background='#fbf9e9' if sub_mn_bg == '' else sub_mn_bg ,
                        foreground='#232323' if sub_mn_fg == '' else sub_mn_fg
                )
        else :
            showerror('Error' , 'sub_mn_text and sub_mn_command must be the same length' )
        return block

    #-------------------------------------------- Label ------------------------------------------
    def __label__ (self  , text = '' , font ='' , width ='' , height ='', bg ='' , fg =''  ):
        label = tk.Label(  master= self.root , 
                           text = text,
                           font= (self.font_default , self.font_default_size) if font == '' else (self.font_default , int(font))  if isinstance(font, int) else (self.font_default,int(font[0]),'bold') if font[1] == 'bold' else font ,
                           width= self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,
                           height =  self.height_normal if height == '' or height == 'normal' else self.height_small if height == 'small'  else  self.height_large if height == 'large' else height ,
                           background= self.root.cget("bg") if bg == '' else bg ,
                           foreground= self.fg_color_default if fg == '' else fg ,
                        )
        return label

    #-------------------------------------------- Input ------------------------------------------
    def __input__ (self  ,ver = '', width ='' , bg ='' , fg ='' ):
        if ver == 1 or ver == '' and self.ver == 1:
            entry = tk.Entry(   master = self.root , 
                                width= self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,
                                background= '#ffffff' if bg == '' else bg ,
                                foreground= self.fg_color_default if fg == '' else fg ,
                            )
            
        elif ver == 2 or ver == '' and self.ver == 2:
            entry = ttk.Entry(  master = self.root ,
                                width= self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,                               
                            )
            
        return entry
    
    #-------------------------------------------- Select ------------------------------------------
    def __select__ (self  ,list_btn =[] , width ='' , bg ='' , fg ='' , font ='' ):
        selected_button = tk.StringVar()
        btn_cb = ttk.Combobox(  self.root, 
                                textvariable= selected_button,
                                width= self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,
                                background= '#ffffff' if bg == '' else bg ,
                                foreground= self.fg_color_default if fg == '' else fg ,
                                font= (self.font_default , self.font_default_size) if font == '' else (self.font_default , int(font))  if isinstance(font, int) else (self.font_default,int(font[0]),'bold') if font[1] == 'bold' else font ,
                            )
        btn_cb['values'] = [i for i in list_btn]
        btn_cb['state'] = 'readonly'

        return btn_cb
    
    #-------------------------------------------- Scroll ------------------------------------------
    def __box_scoll__(self  , text = '' , font ='' , width ='' , height ='', bg ='' , fg ='' , bd_w = ''  , rd_style = '' , cursor = ''):
        block = tk.Frame(  self.root ,
                            borderwidth = self.border_width_default if bd_w == '' else int(bd_w) ,
                            relief = self.relief_default if rd_style == '' else rd_style ,
                            background= self.root.cget("bg") if bg == '' else bg ,
                            height= self.height_normal if height == '' or height == 'normal' else self.height_small if height == 'small'  else  self.height_large if height == 'large' else height ,
                            width= self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,

                         )
        text_box = tk.Text( self.root,
                            height= self.height_normal if height == '' or height == 'normal' else self.height_small if height == 'small'  else  self.height_large if height == 'large' else height ,
                            width= self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,
                            background= '#ffffff' if bg == '' else bg ,
                            foreground= self.fg_color_default if fg == '' else fg ,
                            font= (self.font_default , self.font_default_size) if font == '' else (self.font_default , int(font))  if isinstance(font, int) else (self.font_default,int(font[0]),'bold') if font[1] == 'bold' else font ,
                            cursor = '' if cursor == '' else cursor,
                     )

        scrollbar = ttk.Scrollbar(self.root, orient='vertical', command=text_box.yview)
        text_box.grid(row=0, column=0, sticky=NS , in_ = block)
        scrollbar.grid(row=0, column=1, sticky=NS , in_ = block)

        text_box['yscrollcommand'] = scrollbar.set
        text_box.insert(1.0, text)

        def set_text(text_set) :
            text_box.delete(1.0, END)
            text_box.insert(1.0, text_set)
        def get_text() :
            return text_box.get(1.0, END)
        block.get = get_text
        block.set = set_text

        return block

    #-------------------------------------------- Checkbox ------------------------------------------
    def __checkbox__ (self , text , command = ''  , oncheck = '' , offcheck = ''):
        agreement = tk.StringVar()

        def agreement_changed():
            tk.messagebox.showinfo(title='Result',message= agreement.get())


        checkbutton =ttk.Checkbutton(
                        self.root,
                        text= text,
                        command= command if command != '' else agreement_changed,
                        variable = agreement,
                        onvalue= oncheck if oncheck != '' else int(oncheck) if isinstance(oncheck, int) else 'agree',
                        offvalue= offcheck if offcheck != '' else int(offcheck) if isinstance(offcheck, int) else 'disagree',
                    )
        return checkbutton
    
    #-------------------------------------------- Radio ------------------------------------------
    def __radio__ (self , text , command = ''  , oncheck = '' , offcheck = ''):
        agreement = tk.StringVar()

        def agreement_changed():
            tk.messagebox.showinfo(title='Result',message= agreement.get())


        radiobutton =ttk.Radiobutton(
                        self.root,
                        text= text,
                        command= command if command != '' else agreement_changed,
                        variable = agreement,
                        onvalue= oncheck if oncheck != '' else int(oncheck) if isinstance(oncheck, int) else 'agree',
                        offvalue= offcheck if offcheck != '' else int(offcheck) if isinstance(offcheck, int) else 'disagree',
                    )
        return radiobutton
     #---------------------------------------------- Open File ------------------------------------------   
    def __btn_open_file__(self ,result, text = 'Open File', type_open = [] , width = '' , height = '' ):
        def open_text_file() :
            filetypes = (   
                            ('All files', '*.*'),
                            ('text files', '*.txt')
                            )
            if type_open != [] :
                for x in type_open :
                    filetypes += (
                            (str(x) , "*."+str(x)),
                    )
            filepath = fd.askopenfilename(filetypes = filetypes)
            if filepath:
                return result(filepath)
                
        open_button = self.__btn__(
            text= text,
            command=open_text_file,
            width= width if width != '' else self.width_normal,
            height = height if height != '' else self.height_normal
        )
        
        return open_button

        
    def __open_file__(self , type_open = [] , width = '' , height = ''):
        block = tk.Frame(  self.root )

        text = tk.Text( self.root,
                        height= self.height_normal if height == '' or height == 'normal' else self.height_small if height == 'small'  else  self.height_large if height == 'large' else height ,
                        width= self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width,
                       )

        def open_text_file() :
            filetypes = (   ('text files', '*.txt'),
                            ('All files', '*.*')
                         )
            if type_open != [] :
                for x in type_open :
                    filetypes += (
                            (str(x) , "*."+str(x)),
                    )
                    
            f = fd.askopenfile(filetypes = filetypes)
            # show the open file dialog
            if f != None :  
                text.insert('1.0', f.readlines())


        # open file button
        open_button = self.__btn__(
            text='Open a File',
            command=open_text_file,
            width= 10,
            height = height
        )
        text.grid(column=0, row=0, sticky='e' , in_ = block)
        open_button.grid(column=1, row=0, sticky='w' , in_ = block)

        def get_text() :
            return text.get(1.0, END)
        
        block.get = get_text

        return block
    
    def __btn_Icon__ (self  , command = '' , icon = '' , width = '' ):
        block = tk.Frame(  self.root )
        btn_add_icon = tk.PhotoImage(file = icon)
        btn_add = ttk.Button(
            self.root,
            image = btn_add_icon,
            width = self.width_normal if width == '' or width == 'normal' else self.width_small if width == 'small'  else  self.width_large if width == 'large'  else width ,
            command= lambda : command()
        )
        
        btn_add.image_names = [btn_add_icon]
        btn_add.grid(column=0, row=0, sticky='w' , in_ = block)
        return block
    #---------------------------------------------- Canvas ------------------------------------------
    def __canvas__(self , width = '' , height = '' ):
        block = tk.Frame(  self.root )
        

        return block

if __name__ == '__main__':
    tkinter_custom()
