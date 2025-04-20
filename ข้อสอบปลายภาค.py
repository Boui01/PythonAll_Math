import matplotlib.pyplot as plt
class Fruit:
    def __init__(self,id,name,price,stock):
        self.id = id
        self.name = name
        self.price =  price
        self.stock = stock
        self.capital = price*stock
    def All(self,price,stock):
        self.price = price*stock   
    def info(self):
        return "Id name Price Stock capital'\n{}  {}  {}    {}    {}".format(self.id, self.name,self.price,self.stock,self.capital)
    def show(self):
        return "{} {} {} {} {}".format(self.id,self.name,self.price,self.stock,self.capital)
 
ft1 = Fruit(1,'Fig',20,30)
ft2 = Fruit(2,'Grap',30,40)
ft3 = Fruit(3,'Kiwi',20,33)
ft4 = Fruit(4,'Lychee',40,20)
ft5 = Fruit(5,'Mango',30,40)
ft6 = Fruit(6,'Papaya',10,30)
ft7 = Fruit(7,'Plum',20,10)
ft8 = Fruit(8,'Pear',35,20)
ft9 = Fruit(9,'Orange',50,70)
ft10 = Fruit(10,'Apple',35,30)

Ft1 = ft1.show()
Ft2 = ft2.show()
Ft3 = ft3.show()
Ft4 = ft4.show()
Ft5 = ft5.show()
Ft6 = ft6.show()
Ft7 = ft7.show()
Ft8 = ft8.show()
Ft9 = ft9.show()
Ft10 = ft10.show()
Fta = ft1.capital+ft2.capital+ft3.capital+ft4.capital+ft5.capital+ft6.capital+ft7.capital+ft8.capital+ft9.capital+ft10.capital
#print('\n',Ft1,'\n',Ft2,'\n',Ft3,'\n',Ft4,'\n',Ft5,'\n',Ft6,'\n',Ft7,'\n',Ft8,'\n',Ft9,'\n',Ft10,'\n')

print(ft1.info())#แสดงข้อมูลสินค้า

lists = [] 
lists.append(Ft1),lists.append(Ft2),lists.append(Ft3),lists.append(Ft4),lists.append(Ft5),lists.append(Ft6),lists.append(Ft7),lists.append(Ft8),lists.append(Ft9),lists.append(Ft10)
print(lists)
print('ผลรวมเงินทุนทั้งหมด',int(Fta))

Fta1 = max(ft1.capital,ft2.capital,ft3.capital,ft4.capital+ft5.capital,ft6.capital,ft7.capital,ft8.capital,ft9.capital,ft10.capital)
Fta2 = min(ft1.capital,ft2.capital,ft3.capital,ft4.capital+ft5.capital,ft6.capital,ft7.capital,ft8.capital,ft9.capital,ft10.capital)
Ftaprice = ft1.price,ft2.price,ft3.price,ft4.price,ft5.price,ft6.price,ft7.price,ft8.price,ft9.price,ft10.price
Fta2max = max(Ftaprice)
Fta2min =  min(Ftaprice)
print('รายการสินค้าที่ราคา max =',max(lists),'\n','รายการสินค้าที่ราคา min =',min(lists))
print('Price max',Fta2max,'\n','Price min',Fta2min)
print('ราคาเงินทุนที่ max',Fta1,'\n','ราคาเงินทุนที่ min',Fta2)


names = ['Fig ','Grap','Kiwi','Lychee','Mango','Papaya','Plum','Pear','Orange','Apple']
values = [ft1.stock,ft2.stock,ft3.stock,ft4.stock,ft5.stock,ft6.stock,ft7.stock,ft8.stock,ft9.stock,ft10.stock]

plt.figure(figsize=(10,5))
plt.title('Stock item')
plt.bar(names, values)
plt.show()








