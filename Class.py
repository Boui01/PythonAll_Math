#คลาสคือต้นแบบของวัตถุ Class is the protype of Object (Object คิอสิ่งที่นำไปใช้งานได้)
class Pouint:
    'Point class'
class Line(object):
    'Line class'
class cicle:
    pass
class Rectangle:
    'Rectangle class with comment'

p1 = Pouint()
p1.x,p1.y = 1,2
def getPouuint():
    return(p1.x,p1.y)
print(getPouuint())
print(p1.x)
print(Pouint)

class Point:
    def _int_(self,x=0,y=0):
        self.x = x
        self.y = y
    def reset(self):
        self.x = 0
        self.y = 0
    def info(self):
        return(self.x,self.y)
    def set(self,x,y):
        self.x = x
        self.y = y
        return self
p1 = Point()
p1.set(1,1)
print(p1.info())
print(Point)

import math
class Line:
   def __init__(self, x = 0, y = 0):
     self.x = x
     self.y = y
   def info(self):
     return (self.x,self.y)
   def length(self,point):
     return math.sqrt((self.x - point.y)**2 +(self.x - point.y)**2)

line = Line(3,2)
line2 = Line()
print(line.length(line2))
print(line2.info())

#---------------------------------------------------------------------
class Order:#Order(ตัวเลขคือไอดี)
 def __init__(self, id, date):
     self.id = id
     self.date = date
 def info(self):
     return "Id:{} Date:{}".format(self.id, self.date)
order1 = Order(1,'17/04/2018')
order2 = Order(2,'18/04/2018')
print(order1.info())
print(order2.info())

