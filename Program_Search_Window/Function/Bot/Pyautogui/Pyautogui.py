import pyautogui
from pynput import mouse
import time
class Pyautogui:
    def __init__(self):
        pass
    def click(self , x , y , action = 'Left' , _time = 0) :
        time.sleep(_time)
        pyautogui.click(x,y)
    def hold_click(self , x , y):
        pyautogui.click(x,y,clicks=2)
    def move(self , x , y):
        pyautogui.moveTo(x,y)
    def write(self , text):
        pyautogui.write(text)
    def press(self , key):
        pyautogui.press(key)
    def hotkey(self , key1 , key2):
        pyautogui.hotkey(key1,key2)

    def click_get_position(self):
        self.listener = None
        self.detail = []
        
        if self.listener is None:
            def on_click(x, y, button, pressed):
                if pressed:
                    self.listener.stop()
                    self.detail = [ x , y , button ]
                    self.listener = None
                    return self.detail , self.listener

            # Set up the listener
            self.listener = mouse.Listener(on_click=on_click)
            self.listener.start()
            self.listener.join()
            
            return self.detail

