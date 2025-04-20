def powerOf(x):#ฟังก์ชันพิเศษ
    return x*x

print(powerOf(-2))

#-------------------------------------------------------------------------------

#lambda คือ การเขียนฟังก์ชันแบบง่าย
#sorted คือ หาค่าตำแหน่งสูงสุด
def derivative(f,x,h):
    return(f(x+h)- f(x))/h
doubleOf = lambda x:2*x+2

triagle = (lambda x,y : 0.5*x*y)
print('ฟังก์ชัน lambda')
print(triagle(2,2))#แปลงเป็นฟังก์ชัน
print(derivative(doubleOf,2,0.1))

nums= [100,200,150]
sorted(nums)

products = [('TV','Sumsung',2000),('Fan','Hatari',400),('Radio','Sony',200)]
print(sorted(products,key=lambda x:x[2]))#ตัวที่อยู่ lambda คือตัวแปร หลังอีกคือ ข้อมูล หรือ ข้อกำหนด

powerOf = doubleOf
print(powerOf(4))
#-------------------------------------------------------------------------------

#Map คือ การเปลี่ยนแปลงค่าข้อมูล เช่น จาก list เป็น set แล้วคืนค่าข้อมูลนั้น

nums = [2,4,6]
result = list(map(lambda x : x*2,nums))
print('ฟังก์ชัน MAP')
print(result)

cat = dict({'name':'cat','color':'black'})
Cat = dict(map(lambda x:(x[0],'white'if x[1]=='black'else x[1]),cat.items()))

print(Cat)#การสร้างฟังก์ชันจากใน dict ถ้าตำแหน่งที่ 1 คือ black ให้เป็น white

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [5,6,7]
print([ i+j+k for i,j,k in zip(list1,list2,list3)])

def square(i):
    return i**2
list_sqr = list(map(square, [2, 4, 5]))
print(list_sqr)#ข้างหลังเป็นข้อมูล
#หรือ list_sqr = [x**2 for x in [2,4,5]]
#    print(list_sqr)
#    แสดงเหมือน list_sqr

list_sqr = [x**2 if x>2 else x for x in [2,4,5]]
print(list_sqr)#การใส่เงื่อนไข ถ้า x มากกว่า 2 ให้เอาไปยกกำลัง 2 

dic =[{'title':'python', 'price':200}, {'title': 'ruby', 'price':300}]
list1 =list(map(lambda x : x['title'], dic))#เอาคำใน title ออกมาแต่เป็นตัวพิมเล็ก
list2 =list(map(lambda x : x['price']*10, dic))#เอาคำใน price ออกมาคูณด้วย 10
list3 =list(map(lambda x :x['title'].capitalize(),dic))#เอาคำใน title ออกมาแต่เป็น
                                                       #ตัวพิมใหญ่
list1 = [2,4,6]
list2 = [3,5,7]
list3 = list(map(lambda x,y : x+y, list1, list2))
print(list3)#การนำข้อมูลสองตัวมาบวกกัน list1 = x , list = y
#-----------------------------------------------------------------------------

#Filter คือ การกองข้อมูล เช่น มากกว่า 2 มีกี่ตัวใน [2,4,6]
print('ฟังก์ชั้น Filter')
print(list(filter(lambda x:x>2,[2,4,6])))
#หรือ  list2 = [x for x in [2,4,6] if x>2]#ใช้เงื่อนไข
#     print(list2)

#-----------------------------------------------------------------------------

#Reduce คือ คืนค่าข้อมูลแค่ค่าเดียวและสามารถคำนวน 2 ค่าในฟังก์ชันเดียวกันได้
from functools import reduce
print('ฟังก์ชัน Reduce')
print(reduce(lambda x,y: x+y,[2,4,6,8]))#การบวก 2 ค่า reduce จะบวก 2 ตัวแรกและไปเรื่อยๆ
                                        #2+4 = 6+6 = 12+8 แสดงค่าเป็น 20

nums = [1,2,3,4,5]
sum_sq = reduce(lambda x,y: x*y, filter(lambda x: x%2==0, nums))
print(sum_sq)#การที่เอากองเลขหาร 2 ลงตัวออกมาแล้วนำมาคูณกัน 


lst = [2,3,4,5]
print(reduce(lambda x, y:x+y, map(lambda x: x**2, lst)))#การคำนวนเลข **2 แล้วไปบวกกัน


#-----------------------------------------------------------------------------

#Map Reduce
import re

def tokenize(message):
 message = message.lower() # convert to lowercase
 all_words = re.findall(r"\b\w+\b", message) # extract the words
 return all_words


data = 'data science big data science fiction'
words = data.split()#คำสั่งรวมคำเช่น data science
from collections import Counter
print('ฟังก์ชัน Map and Reduce')
print(Counter(words))#นับตัวซ้ำ เช่น d=1 b=2

def mapper(x):
 return list(map(lambda x: (x,1), tokenize(x)))
words = mapper(data)
for w in words:
    print(w)





