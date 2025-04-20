from Tkinter_custom.tkinter_custom import tkinter_custom 
from Function.Translate_type.MySQL_language import MySQL_language
class Translate :

    def __init__(self ,root , status = '') :
        self.root = root
        self.tk_custom = tkinter_custom( self.root )
        self.status = status

        self.type_translate = ['MySql','Laravel']
        self.btn_main_translate = []
        self.Translate_main()
    def Translate_main(self) :
        selected_label = self.tk_custom.__label__(text = 'Selected ' , font = 18)
        selected_label.grid(row = 0, column = 0)

        block_head = self.tk_custom.__label__(text = '')
        block_head.grid(row = 1, column = 0 )

        selected_label_from = self.tk_custom.__label__(text = 'From : ')
        selected_label_from.grid(row = 0, column = 0 , padx= 10, in_=block_head)
        selected_button_from = self.tk_custom.__select__(list_btn= self.type_translate)
        selected_button_from.grid(row = 1, column = 0  , pady= 10 , padx= 10, in_=block_head)

        selected_label_to = self.tk_custom.__label__(text = 'To : ')
        selected_label_to.grid(row = 0, column = 1  , padx= 10, in_=block_head)
        selected_button_to = self.tk_custom.__select__(list_btn= self.type_translate)
        selected_button_to.grid(row = 1, column = 1  , pady= 10, padx= 10 , in_=block_head)

        self.window_translate = self.tk_custom.__open_file__(type_open = self.type_translate , width= 60 , height = 10)
        self.window_translate.grid(row = 2, column = 0, rowspan = 2, sticky = 'nsew' , padx= 15)

        translate_button = self.tk_custom.__btn__(text = 'Translate', command = lambda: self.Translate_select(From= selected_button_from.get() , To = selected_button_to.get()))
        translate_button.grid(row = 4, column = 0, sticky = 'nsew' , padx= 15)

        self.window_result = self.tk_custom.__box_scoll__(text = '' , width = 80 , height = 10 , cursor= 'left_side' )
        self.window_result.grid(row = 5, column = 0, sticky = 'nsew' , padx= 15)

        back_button = self.tk_custom.__btn__(text = 'Back' , command = self.Back)
        back_button.grid(row = 6, column = 0, sticky = 'nsew', columnspan = 2 , pady = 20)

        self.btn_main_translate.append(selected_label)
        self.btn_main_translate.append(selected_button_from)
        self.btn_main_translate.append(selected_button_to)
        self.btn_main_translate.append(block_head)
        self.btn_main_translate.append(translate_button)
        self.btn_main_translate.append(self.window_result)
        self.btn_main_translate.append(self.window_translate)
        self.btn_main_translate.append(back_button)

    def Translate_select(self, From , To) :
        result = False
        text = ''

        result_translate = MySQL_language( text= self.window_translate.get() ).Translate(From = From)
        result = result_translate['result']
        text = result_translate['text']
        
        if result == True :
            if To == 'MySql' :
                self.Translate_Mysql( text = text )

    def Translate_Mysql(self , text) :
        self.window_result.set(text)

    def Back(self) :
        for i in self.btn_main_translate :
            self.tk_custom.__hide__([i])

        self.status('show')