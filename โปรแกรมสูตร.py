import tkinter as tk

def PG():
    y = int(Q_input.get())
    output = ('\
    import pyautogui as pg'+'\n'+'\
    import time '+'\n'+'\
    --สูตร pg-- '+'\n'+'\
    pg.moveTo(-,-,duration=..)=ใช้เลื่อนเมาส์ '+'\n'+'\
    pg.write('')=ใช้พิมคำตามที่่ใส่ลงไป '+'\n'+'\
    pg.click(-,-)=ใช้คลิก  '+'\n'+'\
    time.sleep(-)=ใช้พัก '+'\n'+'\
    pg.doubleClick = ใช้คลิกสองที '+'\n'+'\
    result = pg.position()การตั้งค่าตำแหน่ง '+'\n'+'\
    pg.dragTo(x,duration =..)=ใช้ลากเมาส์ '+'\n'+'\
    pg.hotkey(''เช่น''ctrl','V','Blackspace'') =ใช้ควบคุมปุ่มคีย์บอร์ด#จะปล่อยคำที่อยู่ทางขวาก่อน '+'\n'+'\
    pg.press(''...'')=ใช้กดปุ่มคีย์บอร์ด '+'\n'+'\
    pg.locateOnScreen('')=ใช้ระบุตำแหน่งโปรแกรมบนหน้าจอ '+'\n'+'\
     สูตร def copytext(เช่น = newline=0 ):=ใช้ copy ใน Layer นั้นๆ '+'\n'+'\
     เช่นวิธีใช้ pg.click(152,151 + newline) '+'\n'+'\
     copytext(เช่น = 54*1 --> 54 x 1)'+'\n'+'\
     ( สามารถใช้ for i in range(10): ) '+'\n'+'\
             copytext(54*i)')\
             if y<=1 else ('\
            \n'+'--สูตรทั่วไป--'+'\n'+'\
    สูตร for i in range' +'\n'+'\
    for i in range(4):' +'\n'+'\
     for i in range(- (=ค่าเริ่มต้น),- (=ค่าสุดท้าย)): =ใช้คำนวนเลขวนรูป เช่น' +'\n'+'\
        print(i)              def = ที่รวบรวมคำสั่ง' +'\n'+'\
     print(i)                               ออกมาเป็น 1 2 3 ' +'\n'+'\
  สูตร def wellcome():เช่น def wellcome(name): =ใช้กรอกข้อมูล' +'\n'+'\
                         print(''ยินดี่ที่ได้รู้จัก'',name)' +'\n'+'\
                         print(''ขอบคุณ'') แล้วกด enter สองครั้้งแล้วพิม wellcome(bou)' +'\n'+'\
    float=() =คำนวณเลขทศนิยม    * = คูณ     ** = ยกกำลัง    % = เอาเศษ  ' +'\n'+'\
    int=() =คำนวณเลขจำนวนเต็ม    / = หาร    // = ตัดเศษทิ้ง   square_root(..)=สแคว์รูท' +'\n'+'\
    True = ถูก   False = ผิด   return =ย้อนกลับ' +'\n'+'\
    วิธีสร้าง facttorail' +'\n'+'\
     def fact (n):' +'\n'+'\
         f = 1' +'\n'+'\
         for i in range(1,n+1):' +'\n'+'\
             f = f*1' +'\n'+'\
' +'\n'+'\
             return f' +'\n'+'\
       n = ---' +'\n'+'\
        print(n)' +'\n'+'\
    if หรือ elif .... >= ... : = ตรวจสอบเงื่อนไข' +'\n'+'\
    วิธีใช้ if' +'\n'+'\
    score = 85  ' +'\n'+'\
       if score >หรือ<หรือมี= 80: ' +'\n'+'\
           print(''Grade A'') ' +'\n'+'\
       elif score >= 70: =ใช้ในการเขียนคำสั่งใน if อีกทีเมื่อเงื่อนไขไม่ตรง' +'\n'+'\
           print(''Grade B'')' +'\n'+'\
    ' +'\n'+'\
    วิธีใช้ ยกกำลัง **          วิธีใช้ square_root' +'\n'+'\
        x = 3                   def square_root(x):' +'\n'+'\
        y = 2                       from math import sqrt' +'\n'+'\
        X = x**y = 6                print(sqrt(x))' +'\n'+'\'')\
        if y<=2 else \
        '\n'+'import turtle =ใช้วาดรูป' +'\n'+'\
        import random =ใช้สุ่ม' +'\n'+'\
        ประกาศ color =[''red'',''yellow'',''blue'',''green'']' +'สูตร for i in range(-):=ใช้วนลูปคำสั่งซ้อนอีกที i=0 ' +'\n'+'\
         for j in range(-):' +'\n'+'\
                 tao.forward((i+1)*--)' +'\n'+'\
                 tao.left(--)' +'\
     สูตร def Rect_size(size = --):=ใช้วาดรูปสีัี่เหลี่ยมแบบเปลี่ยนองศาด้วยหรือเคลื่อนที่รูป' +'\n'+'\
      for i in range(-):' +'\n'+'\
         tao.forward(size)' +'\n'+'\
         tao.left(--)' +'\n'+\
     '\n'+'\
    tao = turtle.Pen() *P ตัวพิมใหญ่      tao.forward()=ขนาดรูป' +'\n'+'\
    tao.shape(''turtle'')     tao.left()=องศารูป' +'\n'+'\
    tao.forward(--)=ใช้เดินไปข้างหน้า' +'\n'+'\
    tao.backward(--)=ใช้เดินไปข้าวหลัง' +'\n'+'\
    tao.right(--)=ใช้เดินไปทางขวา+คุมองศาตามเข็ม' +'\n'+'\
    tao.left(--)=ใช้เดินไปทางซ้าย+คุมองศาทวนเข็ม' +'\n'+'\
    tao.clear()=ใช้เคลียรูปแต่เต่้าจะไม่กลับมาที้่เดิม' +'\n'+'\
    tao.reset()=ใช้เคลียรูปแต่เต่้าจะกลับมาที้่เดิม' +'\n'+'\
    tao.circle(--)=ใช้วาดรูปวงกลม' +'\n'+'\
    tao.goto(--,--)=ใช้เคลื่อนที่เต่า' +'\n'+'\
    tao.penup()=ใช้ให้ปากกาขึ่น' +'\n'+'\
    tao.pendown()=ใช้ให้ปากกาลง' +'\n'+'\
    print(random.randint(--,--))=ใช้สุ่มจำนวนเต็ม' +'\n'+'\
    clr = random.choice(color)=ใช้เลือกสี' +'\n'+'\
    ... = random.choice([--,--])=ใช้เลือกตัวเลข' +'\n'+'\
     '                  '+สูตร for i in range(-):=ใช้วนลูปคำสั่ง' +'\n'+'\
         tao.forward(--)' +'\n'+'\
         tao.left(--)' +'\n'+'\
         ' +'\n'+'\
    >>> for i in range(--):' +'\n'+'\
            Rect_size(--)---> =ขนาด' +'\n'+'\
            tao.left(--) ---> =องศา' +'\
     สูตร for i in range(-):=ใช้วาดวงกลมเเบบเปลี่ยนองศา' +'\n'+'\
         tao.circle(--)' +'\n'+'\
         tao.left(--)' +'\
     สูตร color =[''red'',''yellow'',''blue'',''green''-->ลำดับสี]=ใช้สี' +'\n'+'\
      for i in color:' +'\n'+'\
         print(i) -->enter 2 ที' +'\n'+'\
         ' +'\n'+'\
        for c in color' +'\n'+'\
            print(c) -->enter 2 ที' +'\n'+'\
            ' +'\n'+'\
         for c in color:' +'\n'+'\
             tao.color(c)' +'\n'+'\
             tao.circle(--)' +'\n'+'\
             Rect_size(--)= --->แล้วแต่จะใส่' +'\n'+'\
             tao.left(--)' +'\
     สูตร color =[''red'',''yellow'',''blue'',''green'']=ใช้สีแบบสุ่ม' +'\n'+'\
      print(random.choice(color))-->แล้ว enter 1 ครั้ง' +'\n'+'\
    ' +'\n'+'\
      for i in range(--)---->รอบที่จะหมุน' +'\n'+'\
         tao.circle(--)' +'\n'+'\
         clr = random.choice(color)' +'\n'+'\
         tao.color(clr)' +'\n'+'\
         tao.left(--)' +'\
     สูตร multisize(แล้วแต่จะพิม) = random.choice([--,--]) =วิธีใช้เลือกตัวเลข' +'\n'+'\
          tao.circke(multisize)' +'\n'+'\
          tao.forward(multisize)' +'\n'+'\
    '
    Q_output.configure(text=output)

window = tk.Tk()
window.title('โปรแกรมคำนวณความน่าจะเป็น')
window.minsize(width=500,height=500)

Q_input = tk.Entry(master=window)
Q_input.pack(pady=10)

Q_button = tk.Button(master=window,text='Enter',width=10,command=PG,bg='#FFCC99')
Q_button.pack(pady=10)

Q_output = tk.Label(master=window,bg='#FFFFCC')
Q_output.pack(pady=10)
