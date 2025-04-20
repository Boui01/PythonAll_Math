r'match'#match เฉพาะตัวที่เขียนเข้าไป
r'[abc]'#match ตัวใดตัวนึงใน a b c
r'[^abc]' #ใช้ match กับตัวที่ไม่ใช่ตัวที่พิมไว้
^ #ตำแหน่งเริ่มต้นของ string 
$ #ตำแหน่งจบของ string
| #ใช้แทนคำว่าหรือ
เครื่องหมายพวกนี้ต้องการตัวอยู่ข้างหน้าก่อร
+ #1 ตัวขึ้นไป
* #0 ตัวขึ้้นไป(ไม่มัก็ได้)
? #0 หรือ 1 ตัว
{m} #ต้องเท่ากับตัวที่ใส่ลงไป เด้ะๆเลย
{m,n}#ตั้งแต่ m ถึง n ตัว
เช่น
r'a+' #จะได้ 'a' 'aa' 'aaa' ต้องการ a 1 ตัวขึ้นไป
r'a*' #จะได้ '' 'a' 'aa' ต้องการตั้งแต่ a 0 ตัวขึ้นไป
r'a?' #จะได้ '' 'a' ต้องการตั้งแต่ a 0 หรือ 1 ตัว
r'a{1,3}' #จะได้ 'a' 'aa' 'aaa' ต้องการแค่ 1 ถึง 3 ตัว
() #ใช้จับกลุ่มตัวอักษร เช่น r'(abc)+' จะเป็น 'abc' 'abcabc'
. #ตัวอักษรอะไรก็ได้ 1 ตัว
\. #ต้องการตัวอักษร .
\d #ตัวอักษรที่เป็นตัวเลข 0-9 1ตัว
\D #ตัวอักษรที่ไม่ใช่ตัวเลข 0-9 1ตัว
\w #ตัวอักษร alphanumeric 1 ตัว
\W #ตัวอักษรที่ไม่ใช่ alphanumeric 1 ตัว
#alphanumeric คือ ตัวอักษรตัวเลข ไม่ใช่เครื่องหมายอะไรทั้งหมด
A-Z #ตัวอักษร 1 ตัว ที่มีค่า unicode ตั้งแต่ A-Z (A,B,C...,Z)
a-z #ตัวอักษร 1 ตัว ที่มีค่า unicode ตั้งแต่ a-z (a,b,c...,z)

วิธีนำมาใช้
import re
re.match #ทำการ match regex จากจุดเริ่มต้นของ string
re.search #ทำการ match regex จากจุดเใดก็ได้ของ string
re.sub #ใช้แทนค่า substring ที่ match regex ด้วยค่าใหม่
re.split #แบ่ง string ด้วย pattern
re.findall() #ใช้ หา substring ทั้งหมดที่ match pattern

import re
text = 'Hello world'
pattern = r'^(Hello|hello).*(world|World)$'
result = re.search(pattern,text)
print(result.group())

text = 'test.@email.com'
pattern = '\w+@\w+\.(com|net)'
result = re.match(pattern,text)
if result is None:
    print('no match')

#วงเล็บแรกจะนับเป็นกลุ่ม 1 และ ต่อไปก็นับไปเรื่อยๆ
text = 'test@email.com'
pattern = '(\w+)@(\w+\.(com|net))'
result = re.match(pattern,text)
print(result.group(1))
print(result.group(2))
#วิธีตั้งชื่อ group (?P<name>\w+)@(?P<domain>\w+\.(com|net))

text = 'blue socks and red shoes'
replace = 'black'
pattern = '(blue|red|green)'
result = re.sub(pattern,replace,text)
print(result)#ตรงกลางคือคำที่จะใช้เปลี่ยน

text = 'boy or girl and dog'
pattern = 'and|or'
res = re.split(pattern,text)
print(res)#ลบคำนั้้นออก

text = '12 dogs,11 cats, 1 egg'
pattern = '\d+'
res = re.findall(pattern,text)
print(res)#เลิอกตัวในลูกน้ำได้

