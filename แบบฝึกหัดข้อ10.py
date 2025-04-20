data = (1,2,3,4,5,5)

data3 = data[4:6]
data4 = data[0:1]
data5 = data[2:3]
data6 = data[4:5]
data7 = data[5:6]
data8 = data[0:6]
print('ความถี่ของ 1 คือ %d' % len(data4))
print('ความถี่ของ 2 คือ %d' % len(data5))
print('ความถี่ของ 3 คือ %d' % len(data6))
print('ความถี่ของ 4 คือ %d' % len(data7))
print('ความถี่ของ 5 คือ %d' % len(data3))
print('ผลรวมความถี่ทั้งหมด คือ %d'% len(data8))
Data = int('%d'% len(data4))
Data1 = int('%d'% len(data5))
Data2 = int('%d'% len(data6))
Data3 = int('%d'% len(data7))
Data4 = int('%d'% len(data3))
Data5 = Data/6,Data1/6,Data2/6,Data3/6,Data4/6
Data6 = sum(Data5)
print('ผลรวมของซิกม่า i ถึง 0 คือ','%.0f'%Data6)


