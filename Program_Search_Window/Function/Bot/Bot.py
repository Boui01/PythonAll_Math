from Tkinter_custom.tkinter_custom import tkinter_custom
from Function.Bot.CV2_Image.CV2_Image import CV2_Image
from tkinter import *
import tkinter as tk
from tkinter.messagebox import  showinfo
from tkinter import ttk
import os
from Function.Bot.Pyautogui.Pyautogui import Pyautogui
from Function.Bot.Timedate import time_until_next

class Bot:

    def __init__(self , root , status) :
        self.root = root
        self.root.minsize(width=400,height=150)
        self.status = status
        self.tk_custom = tkinter_custom( tk =  self.root )
        self.date = time_until_next
        self.py_gui = Pyautogui()
        self.time = 0
        self.count_add = 0

        
        self.list_btn_main = []
        
        self.list_btn_bot_image = []
        self.list_btn_bot_click = []
        
        self.list_path = []
        self.list_action = []

        self.Bot_main()
        self.Position()        
        pass
    
    def Bot_main(self):
        btn_bot_image = self.tk_custom.__btn__( text = 'Bot Image' , width = 'normal' , height= 'small' , command = lambda : (self.Position_Bot_Image() , self.Close_btn_main()) )
        btn_bot_click = self.tk_custom.__btn__( text = 'Bot Click' , width = 'normal' , height= 'small' , command = lambda : (self.Position_Bot_Click() , self.Close_btn_main()) )
        btn_back = self.tk_custom.__btn__( text = 'Back' , width = 'normal' , height= 'small' , command = self.Back )
                
        self.list_btn_main.append( btn_bot_image )
        self.list_btn_main.append( btn_bot_click )
        self.list_btn_main.append( btn_back )

        
        self.Bot_image()
        self.Bot_click()

    
    def Bot_image(self):
        def Detect_image( path = ''):
            for p in path:
                cv2 = CV2_Image( p['time'] )
                template_image_path = p['path'] 
                
                if not os.path.exists(template_image_path):
                    print(f"File not found: {template_image_path}")
                else:
                    print(f"File exists: {template_image_path}")
                    cv2.detect_position_click(template_image_path)
            self.list_path.clear()
               
        btn_open_img = self.tk_custom.__btn_open_file__( result= lambda path :  (   self.list_path.append({ 'path' : path , 'time' : 0 if time_limit.get() == '' else int(time_limit.get() * 60 * 60 if time_select.get() == 'Hour' else time_limit.get() * 60 if time_select.get() == 'Minute' else time_limit.get())  }) , 
                                                                                    time_label.config(text= f'Time : {'0 Second' if time_limit.get() == '' else time_limit.get()+' '+time_select.get()} \n at '+self.date( 0 if time_limit.get() == '' else int(time_limit.get()) , time_select.get() ))
                                                                                ) ,
                                                                                    text = 'Open Image',
                                                                                    type_open = ['jpg' , 'png'] ,
                                                                                    width = 'normal' ,
                                                                                    height = 'small' 
                                                        )
        btn_confirm = self.tk_custom.__btn__( text = 'Confirm' , width = 'normal' , height= 'small' , command = lambda : Detect_image( self.list_path   ) )
        btn_back = self.tk_custom.__btn__( text = 'Back' , width = 'normal' , height= 'small' , command = self.Back_Bot_Image )
        btn_add = self.tk_custom.__btn_Icon__(
            icon = './Icon/icons8-add-blue-ui-32.png',
            width = 'normal',
            command = lambda : self.Add_function('bot_image')
        )
        

        time_label = self.tk_custom.__label__( text = 'Time : ' , width = 'large' , height = 4 )
        time_limit = self.tk_custom.__input__( ver = 2  , width = 'normal' ) 
        time_select = self.tk_custom.__select__(
            width = 'normal' ,
            list_btn = ['Hour' , 'Minute' , 'Second']
        )
  
        
 
        # Add list btn
        self.list_btn_bot_image.append( {'id' : self.count_add , 'data' : btn_open_img} )
        self.list_btn_bot_image.append( {'id' : self.count_add , 'data' : btn_confirm} ) if self.count_add == 0 else None
        self.list_btn_bot_image.append( {'id' : self.count_add , 'data' : btn_back} )
        self.list_btn_bot_image.append( {'id' : self.count_add , 'data' : btn_add} )
        
        self.list_btn_bot_image.append( {'id' : self.count_add , 'data' : time_label} )
        self.list_btn_bot_image.append( {'id' : self.count_add , 'data' : time_limit} )
        self.list_btn_bot_image.append( {'id' : self.count_add , 'data' : time_select} )

    def Bot_click(self):
        def Confirm_Value_Click():
            count_loop = 0
            for i in range( int(len(self.list_btn_bot_click)/15)):
                if self.list_btn_bot_click[1 + count_loop]['data'].get() != '' or self.list_btn_bot_click[2 + count_loop]['data'].get() != '':
                    self.list_action.append({ 
                        'id' : self.list_btn_bot_click[0 + count_loop]['id'],
                        'set_1' : { 'x' : int( self.list_btn_bot_click[1 + count_loop]['data'].get() ),
                                    'y' : int( self.list_btn_bot_click[2 + count_loop]['data'].get() )
                                },
                        'set_2' : { 'x' : int( self.list_btn_bot_click[12 + count_loop]['data'].get() ) if self.list_btn_bot_click[12 + count_loop]['data'].get() != '' else 0 ,
                                    'y' : int( self.list_btn_bot_click[13 + count_loop]['data'].get() ) if self.list_btn_bot_click[13 + count_loop]['data'].get() != '' else 0
                                },
                        'action' : self.list_btn_bot_click[6 + count_loop]['data'].get(),
                        'form' : self.list_btn_bot_click[5 + count_loop]['data'].get(),
                        'duration' : int( self.list_btn_bot_click[8 + count_loop]['data'].get() ) if self.list_btn_bot_click[8 + count_loop]['data'].get() != '' else 0
                    })
                    count_loop += 15
                else :
                    showinfo( 'Error' , 'Please fill all field' )
                    break
                
            for i in self.list_action :
                if i['form'] == 'Click' :
                    self.py_gui.click( i['set_1']['x'] , i['set_1']['y'], i['action'] , i['duration'] )
                    if i['set_2']['x'] != 0 and i['set_2']['y'] != 0 :
                        self.py_gui.click( i['set_2']['x'] , i['set_2']['y'], i['action'] , i['duration'] ) 
                           
            self.list_action.clear()                      
            print(self.list_action )
                    
        def SetValue_Check_Position():
            detial = self.py_gui.click_get_position()
            if move_x_click.get() == '' or move_y_click.get() == '':
                move_x_click.insert(0,detial[0])
                move_y_click.insert(0,detial[1])
            else :
                move_x_click_2.insert(0,detial[0])
                move_y_click_2.insert(0,detial[1])
                
            showinfo( 'Position' , f'X : {detial[0]} Y : {detial[1]} \nButton : {detial[2]}' )

            
        self.root.minsize(width=400,height=180)
        
        move_label = self.tk_custom.__label__( text = 'SET 1 : ' , width = 'large' , height = 'small' )
        move_x_click = self.tk_custom.__input__( ver = 2  , width = 'large' , bg = '#ffffff' )
        move_y_click = self.tk_custom.__input__( ver = 2  , width = 'large' , bg = '#ffffff' )
        move_label_2 = self.tk_custom.__label__( text = 'SET 2 : ' , width = 'large' , height = 'small' )
        move_x_click_2 = self.tk_custom.__input__( ver = 2  , width = 'large' , bg = '#ffffff' )
        move_y_click_2 = self.tk_custom.__input__( ver = 2  , width = 'large' , bg = '#ffffff' )
        
        select_action = self.tk_custom.__select__(
            width = 'normal' ,
            list_btn = ['Left' , 'Center' , 'Right']
        )
        select_label = self.tk_custom.__label__( text = 'STATE ' +str(self.count_add) +'\nSelect Action : ' , width = 'large' , height = 'normal' )
        select_form = self.tk_custom.__select__(
            width = 'normal' ,
            list_btn = ['Click' , 'Hold' , 'Scroll']
        )
        duration_lable = self.tk_custom.__label__(  text = 'Duration ' , width = 'large' , height = 'small' )
        input_duration = self.tk_custom.__input__( ver = 2  , width = 'large' , bg = '#ffffff' )
        add_btn = self.tk_custom.__btn_Icon__(
            icon = './Icon/icons8-add-blue-ui-32.png',
            width = 'normal',
            command = lambda : self.Add_function('bot_click')
        )
        check_position = self.tk_custom.__btn__( text = 'Check position' , width= 'large' , height = 'small' ,command= lambda : SetValue_Check_Position() )
        confirm = self.tk_custom.__btn__( text = 'Confirm' , width = 'normal' , height= 'small' , command = Confirm_Value_Click  )
        back = self.tk_custom.__btn__( text = 'Back' , width = 'normal' , height= 'small' , command = self.Back_Bot_Click )

        
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : move_label} )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : move_x_click } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : move_y_click } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : back  if self.count_add == 0 else None   } )        
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : select_label } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : select_form } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : select_action } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : duration_lable } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : input_duration } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : check_position } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : add_btn } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : move_label_2 } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : move_x_click_2 } )
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : move_y_click_2 } )        
        self.list_btn_bot_click.append( {'id' : self.count_add , 'data' : confirm  if self.count_add == 0 else None } )       




    #----------------------------------------------------Add------------------------------------------------------
    def Add_function(self , function):
        self.count_add += 1
        
        if function == 'bot_image':
            self.Bot_image()
            self.Position_Bot_Image()
        elif function == 'bot_click':
            self.Bot_click()
            self.Position_Bot_Click()
            
        return self.count_add

    #----------------------------------------------------Position------------------------------------------------------
    def Position(self):
        x = 0
        y = 0
        self.count_add = 0
        for btn in self.list_btn_main :
            btn.grid( column = x , row = y , padx = 5 , pady = 5 )  
            y += 1         
            if y == 4 :
                x += 1
                y = 0
        return self.count_add

    def Position_Bot_Image(self):
        x = 0
        y = 0
        count = 0
        count_add = 0
        for btn in self.list_btn_bot_image :
            btn['data'].grid( column = x , row = y , padx = 5 , pady = 5 )  
            y += 1         
            if count_add == 0 and y == 4 :
                x += 1
                y = 0
                count += 1
                count_add += 1
            elif count == 1:
                y = 0
                x += 1
                count += 1
            elif count == 2 and  y == 2 :
                y = 0
                x += 1
                count = 0
            elif count_add != 0 and  y == 3 :
                x += 1
                y = 0
                count += 1
                    
    def Position_Bot_Click(self):
        x = 0
        y = 0
        y_add = 0
        count = 0
        count_add = 0
        for btn in self.list_btn_bot_click :
            if btn['data'] != None :
                btn['data'].grid( column = x , row = y , padx = 5 , pady = 5 )  
            y += 1         
            if count == 0 and x <= 8  :
                if y > 3 + y_add :
                    x += 1
                    y = 0 + y_add
                    count += 1
                elif y > 2 + y_add :
                    y += 4

            if count == 1 and y > 6 + y_add and x <= 8  :
                y = 0 + y_add
                x += 1
                count += 1
            elif count == 2  and x <= 8 : 
                if y > 3 + y_add  and x < 8 :
                    x += 1
                    y = 0 + y_add
                    count = 0
                    count_add += 1
                elif y > 3 + y_add  and  x == 8 :
                    x = 0
                    y_add += 7
                    y = y_add  
                    count = 0    
                elif y > 2 + y_add :
                    y += 4    
                

      
    #----------------------------------------------------Back------------------------------------------------------
    def Back(self):
        for i in self.list_btn_main:
            i.grid_remove()
        self.status( status = 'show' )
    def Back_Bot_Image(self):  
        for i in self.list_btn_bot_image:
            i['data'].grid_remove()

        self.Position()

    def Back_Bot_Click(self):
        for i in self.list_btn_bot_click:
            i['data'].grid_remove() if i['data'] != None else None
            
        self.Position()
        
    def Close_btn_main(self):
        for i in self.list_btn_main:
            i.grid_remove()
            

