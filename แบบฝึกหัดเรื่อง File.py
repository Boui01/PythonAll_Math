import pickle
import csv
def demo():
    dogs_dict = [{ 'title': {'C# Programing': {'price': 100}}, 'available': True, 'isbn': None },
    { 'title':{ 'Python':{ 'price': 110}}, 'available': True, 'isbn': None} ,
     { 'title':{ 'Java':{ 'price': 120}}, 'available': False, 'isbn': 123123333 }]
    with open('dog_dict.csv','w',newline='',encoding='utf8')as f:
        fw = csv.writer(f)
        fw.writerow(dogs_dict)
demo()

lines = [line for line in open("dog_dict.csv")]
line = lines[0]
print(line)


#วิธีที่ 2

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
print("\nโจทย์ที่่จารใส่ไว้มันอ่านไม่ออกครับ ผมเลยใส่วงเล็บเข้าไปไม่งั้นรันไม่ได้ครับมันเลยไม่แยก")
