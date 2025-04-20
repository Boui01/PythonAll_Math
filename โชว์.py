import pyautogui as pg
import time
pg.moveTo(58,780,duration=3)
pg.hotkey('k',duration=3)
pg.hotkey('u',duration=3)
pg.hotkey('y',duration=3)
pg.hotkey('b',duration=3)
pg.hotkey('i',duration=3)
pg.hotkey('g',duration=3)
pg.hotkey('m',duration=3)
pg.hotkey('a',duration=3)
pg.hotkey('k',duration=3)
pg.hotkey(' ',duration=3)
time.sleep(1)
x=(64,780)
pg.click(x)
y=(189,780)
pg.dragTo(y,duration=1)
pg.hotkey('ctrl','c')
pg.moveTo(215,780,duration=1)
pg.click(215,780)
pg.hotkey('ctrl','v',duration=3)
pg.hotkey(' ',duration=3)
pg.hotkey('ctrl','v',duration=3)
pg.hotkey(' ',duration=3)
pg.hotkey('ctrl','v',duration=3)



