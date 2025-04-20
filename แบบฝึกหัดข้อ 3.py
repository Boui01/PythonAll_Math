class Order:
 def __init__(self, id, date,price):
     self.id = id
     self.date = date
     self.price = price
 def info(self):
     return "Product:{} Date:{} Price:{}".format(self.id, self.date, self.price)
 def allprice(self):
     self.allprice = self.price
     return self.allprice
     
Product1 = Order(1,'01/02/2021',100)
Product2 = Order(2,'02/03/2021',200)
Product3 = Order(3,'03/04/2021',300)

class Product:
    OD = 1
    def __init__(self):
         self.id = Product.OD
         Product.OD +=1
         self.orders = []
    def info(self):
         orderInfo = ""
         for order in self.orders:
             orderInfo+= order.info() +"\n"
         return "Order Id:{}\nProduct:\n{}".format(self.id, orderInfo)
    def addOrder(self, order):
        self.orders.append(order)
        return self

PD = Product()
PD.addOrder(Product1).addOrder(Product2).addOrder(Product3)
ALLPRICE = Product1.allprice()+Product2.allprice()+Product3.allprice()

print(PD.info())
print('ALL PRICE :',ALLPRICE)


