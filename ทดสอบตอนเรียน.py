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