import pyautogui as pg
import time
time.sleep(2)
for i in range(482):
    pg.hotkey('TAB')
    pg.hotkey('left')
    pg.hotkey('left')
    pg.hotkey('left')
    pg.hotkey('left')
    pg.hotkey('down')
    print(i)
