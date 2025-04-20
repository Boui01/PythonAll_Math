a1 = 
a2 = 
a3 = 
a4 = 
a5 = 
a6 = 
a7 = 
a8 = 
a9 = 
a10 = 
#a11 =
#a12 =
#a13 =
#a14 =
#a15 =
#a16 =
#a17 =
#a18 =
#a19 =
#a20 =
b = 
a = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10#+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20
x = a/b
print('x =',x)
print('----เลข x-x----')
########สูตรหา เอ็กลบเอ็ก
X1 = a1-x
X2 = a2-x
X3 = a3-x
X4 = a4-x
X5 = a5-x
X6 = a6-x
X7 = a7-x
X8 = a8-x
X9 = a9-x
X10 = a10-x
#X11 = a11-x
#X12 = a12-x
#X13 = a13-x
#X14 = a14-x
#X15 = a15-x
#X16 = a16-x
#X17 = a17-x
#X18 = a18-x
#X19 = a19-x
#X20 = a20-x
for i in range(1):
    print('X1=',X1,'/','X2=',X2,'/','X3=',X3,'/','X4=',X4,'/','X5=',X5,'/')
    print('X6=',X6,'/''X7=',X7,'/','X8=',X8,'/')
    print('X9=',X9,'/','X10=',X10,'/',)
    #print('X11=',X11,'X12=',X12)
    print('--- ยกกำลัง 2---')
############สูตรหา ยกกำลัง 2 
XX0 = 2
XX1 = X1**XX0
XX2 = X2**XX0
XX3 = X3**XX0
XX4 = X4**XX0
XX5 = X5**XX0
XX6 = X6**XX0
XX7 = X7**XX0
XX8 = X8**XX0
XX9 = X9**XX0
XX10 = X10**XX0
#XX11 = X11**XX0
#XX12 = X12**XX0
#XX13 = X13**XX0
#XX14 = X14**XX0
#XX15 = X15**XX0
#XX16 = X16**XX0
#XX17 = X17**XX0
#XX18 = X18**XX0
#XX19 = X19**XX0
#XX20 = X20**XX0
for i in range(1):
    print('XX1=',XX1,'/','XX2=',XX2,'/','XX3=',XX3,'/','XX4=',XX4,'/','XX5=',XX5,'/')
    print('XX6=',XX6,'/','XX7=',XX7,'/','XX8=',XX8,'/')
    print('XX9=',XX9,'/','XX10=',XX10,'/')
    #print('XX11=',XX11,'/','XX12=',XX12,'/','XX13=',XX13,'/','XX14=',XX14,'/','XX15=',XX15,'/')
    #print('XX16=',XX16,'/','XX17=',XX17,'/','XX18=',XX18,'/','XX19=',XX19,'/','XX20=',XX20,'/')
    print('----ผลรวม ยกกำลัง 2----')
XXX = XX1+XX2+XX3+XX4+XX5+XX6+XX7+XX8+XX9+XX10#+XX11+XX12+XX13+XX14+XX15+XX16+XX17+XX18+XX19+XX20
print(XXX)

B = b-1
def square_root(x):
	from math import sqrt
	print(sqrt(x))

print('ผลรวมยกกำลัง 2 /',XXX,'ส่วน',b,'-1 =')
Sx= square_root(XXX/b)

print('------ค่าสัมประสิทธิ์-----')
print('Sx ส่วนด้วย',x)

