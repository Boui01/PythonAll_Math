import pyautogui as pg
import time
--สูตร pg--
pg.moveTo(-,-,duration=..)=ใช้เลื่อนเมาส์
pg.write('')=ใช้พิมคำตามที่่ใส่ลงไป
pg.click(-,-)=ใช้คลิก
time.sleep(-)=ใช้พัก
pg.doubleClick = ใช้คลิกสองที
result = pg.position()การตั้งค่าตำแหน่ง
pg.dragTo(x,duration =..)=ใช้ลากเมาส์
pg.hotkey('เช่น'ctrl','V','Blackspace'') =ใช้ควบคุมปุ่มคีย์บอร์ด#จะปล่อยคำที่อยู่ทางขวาก่อน
pg.press('...')=ใช้กดปุ่มคีย์บอร์ด
pg.locateOnScreen('')=ใช้ระบุตำแหน่งโปรแกรมบนหน้าจอ
 สูตร def copytext(เช่น = newline=0 ):=ใช้ copy ใน Layer นั้นๆ
     เช่นวิธีใช้ pg.click(152,151 + newline )
     copytext(เช่น = 54*1 --> 54 x 1)
     ( สามารถใช้ for i in range(10): )
             copytext(54*i)
 
#################################################################################
--สูตรทั่วไป--
  สูตร for i in range                           for i in range(4):
     for i in range(- (=ค่าเริ่มต้น),- (=ค่าสุดท้าย)): =ใช้คำนวนเลขวนรูป เช่น    print(i)              def = ที่รวบรวมคำสั่ง
     print(i)                               ออกมาเป็น 1 2 3 
  สูตร def wellcome():เช่น def wellcome(name): =ใช้กรอกข้อมูล
                         print('ยินดี่ที่ได้รู้จัก',name)
                         print('ขอบคุณ') แล้วกด enter สองครั้้งแล้วพิม wellcome(bou)
    float=() =คำนวณเลขทศนิยม    * = คูณ     ** = ยกกำลัง    % = เอาเศษ  '%.2f'%__=แสดงทศนิยม 2 ตำแหน่ง
    int=() =คำนวณเลขจำนวนเต็ม    / = หาร    // = ตัดเศษทิ้ง   square_root(..)=สแคว์รูท
    True = ถูก   False = ผิด   return =ย้อนกลับ
    วิธีสร้าง facttorail
     def fact (n):
         f = 1
         for i in range(1,n+1):
             f = f*1

             return f
       n = ---
        print(n)
    if หรือ elif .... >= ... : = ตรวจสอบเงื่อนไข
    วิธีใช้ if                      
    score = 85                           
       if score >หรือ<หรือมี= 80:           
           print('Grade A') 
       elif score >= 70: =ใช้ในการเขียนคำสั่งใน if อีกทีเมื่อเงื่อนไขไม่ตรง
           print('Grade B')

    วิธีใช้ ยกกำลัง **          วิธีใช้ square_root
        x = 3                   def square_root(x):
        y = 2                       from math import sqrt
        X = x**y = 6                print(sqrt(x))
################################################################################                         

import turtle =ใช้วาดรูป
import random =ใช้สุ่ม
ประกาศ color =['red','yellow','blue','green']

    tao = turtle.Pen() *P ตัวพิมใหญ่      tao.forward()=ขนาดรูป
    tao.shape('turtle')     tao.left()=องศารูป
    tao.forward(--)=ใช้เดินไปข้างหน้า
    tao.backward(--)=ใช้เดินไปข้าวหลัง
    tao.right(--)=ใช้เดินไปทางขวา+คุมองศาตามเข็ม
    tao.left(--)=ใช้เดินไปทางซ้าย+คุมองศาทวนเข็ม
    tao.clear()=ใช้เคลียรูปแต่เต่้าจะไม่กลับมาที้่เดิม
    tao.reset()=ใช้เคลียรูปแต่เต่้าจะกลับมาที้่เดิม
    tao.circle(--)=ใช้วาดรูปวงกลม
    tao.goto(--,--)=ใช้เคลื่อนที่เต่า
    tao.penup()=ใช้ให้ปากกาขึ่น
    tao.pendown()=ใช้ให้ปากกาลง
    print(random.randint(--,--))=ใช้สุ่มจำนวนเต็ม
    clr = random.choice(color)=ใช้เลือกสี
    ... = random.choice([--,--])=ใช้เลือกตัวเลข
    
 สูตร for i in range(-):=ใช้วนลูปคำสั่ง
         tao.forward(--)
         tao.left(--)
 สูตร for i in range(-):=ใช้วนลูปคำสั่งซ้อนอีกที i=0 
         for j in range(-):
                 tao.forward((i+1)*--)
                 tao.left(--)
 สูตร def Rect_size(size = --):=ใช้วาดรูปสีัี่เหลี่ยมแบบเปลี่ยนองศาด้วยหรือเคลื่อนที่รูป
      for i in range(-):
         tao.forward(size)
         tao.left(--)

    >>> for i in range(--):
            Rect_size(--)---> =ขนาด
            tao.left(--) ---> =องศา
 สูตร for i in range(-):=ใช้วาดวงกลมเเบบเปลี่ยนองศา
         tao.circle(--)
         tao.left(--)
 สูตร color =['red','yellow','blue','green'-->ลำดับสี]=ใช้สี
     for i in color:
         print(i) -->enter 2 ที
         
        for c in color
            print(c) -->enter 2 ที
            
         for c in color:
             tao.color(c)
             tao.circle(--)
             Rect_size(--)= --->แล้วแต่จะใส่
             tao.left(--)
 สูตร color =['red','yellow','blue','green']=ใช้สีแบบสุ่ม
     print(random.choice(color))-->แล้ว enter 1 ครั้ง

     for i in range(--)---->รอบที่จะหมุน
         tao.circle(--)
         clr = random.choice(color)
         tao.color(clr)
         tao.left(--)
 สูตร multisize(แล้วแต่จะพิม) = random.choice([--,--]) =วิธีใช้เลือกตัวเลข
          tao.circke(multisize)
          tao.forward(multisize)
##########################################################################
---สูตรสร้างโปรแกรม----
import tkinter as tk

window = tk.Tk() 
window.title('') =ชื่อโปรแกรม
window.minsize(width=--,height=--) =ขนาดโปรแกรม
window.configure(background='#FFFFCC')#ตั้งสีพื้นหลัง

----.configure(text=....)=ใช้เปลี่ยนค่า
.pack(pady= ความห่าง,width= ความกว้่าง,height= ความสูง)
.grid(row= , column = )= ใช้วางตำแหน่งแบบคอรั่ม
.place(x= ,y= )= ใช้วางตำแหน่งเป็นแกน
,font=('Tahoma',ขนาด)= ปรับขนาดตัวหนังสือ
Q_label = tk.Label(master=window,text='วันจันทร์',bg='#FFFFCC',fg='black')#ใช้ตั้งสี
Q_label.pack()

photo = PhotoImage(file='3.png')#ใช้ตั้งปุ่มเป็นรูป
Button(window,text='Enter',image=photo,width=10).pack()
window.mainloop()

title_label = tk.Label(master=window,text='')=ข้อความในโปรแกรม
title_label.pack()=ใช้แสดงในโปรแกรม

number_input = tk.Entry(master=window)=ช่องว่างให้เติมในโปรแกรม
number_input.pack(pady=-- = เลื่อนตำแหน่งข้อความในแนวตั้ง)=ใช้แสดงในโปรแกรม

go_button = tk.Button(master=window,text=''#ไม่จำเป็นต้องใส่,
                      command=...=คำสั่ง
                      )=ปุ่มกดคลิก
go_button.pack()=ใช้แสดงในโปรแกรม

output_output = tk.Label(master=window)
output_output.pack()
 สูตร
.... =int(number_input.get) =ใช้ใส่ในสูตรเพื่อคำนวณคำทืี่ใส่ในช่องว่างแปลงเป็นตัวเลข
 เช่้น
def show_output():
    number = int(number_input.get())

    output = ''
    for i in range(1,13):
        output += str(number) + 'x' + str(i)
        output += ' = ' + str(number * i)+'\n'

    output_label.configure(text=output)



window.mainloop() =แสดงโปรแกรม    
    
