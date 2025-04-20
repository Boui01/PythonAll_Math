#File
#'r' ใช้อ่านอย่างเดียว'
#'w' ใช้กับการเขียนไฟล์ใหม่แต่ถ้าเขียนทับด้วยตัวนี้จะเอาแค่อันใหม่
#'a' ใช้เขียนต่อจากไฟล์เก่า

#เขียนไฟล์ใหม่ผ่าน python
p1 = open('myfile.txt',mode='w') 
p2 = 'This is the frist line.\n'
p1.write(p2)
p3 = 'This is the second line.\n'
p1.write(p3)
p1.close()

with open('myfile.txt','a')as f:
    p4 = 'This is the third line.\n'
    f.write(p4)
#ฟังก์ชัน os
import os
path = os.path.abspath('myfile.txt')
file = open(path,'a')
line4 = 'This is the forth line.\n'
file.write(line4)
file.close()

#ฟังก์ชัน pickle ใช้แพ็คไฟล์
import pickle
dogs_dict = [{ 'title': {'C# Programing': {'price': 100}}, 'available': True, 'isbn': None },
    { 'title':{ 'Python':{ 'price': 110}}, 'available': True, 'isbn': None} ,
     { 'title':{ 'Java':{ 'price': 120}}, 'available': False, 'isbn': 123123333 }]

filename = 'dogs.csv'
outfile = open(filename, 'wb')
pickle.dump(dogs_dict, outfile)
outfile.close()

infile=open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))

#ฟังก์ชัน bz2 ใช้บีบอัดไฟล์ให้เล็กมากๆ
import bz2
import pickle
dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12,
'Balou': 9, 'Laika': 16 }
sfile = bz2.BZ2File('smallerfile', 'w')
pickle.dump(dogs_dict, sfile)
sfile.close()


