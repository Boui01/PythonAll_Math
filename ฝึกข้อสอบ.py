import re
import string
number = [1,2,3,'-','+','d']
Number = []
def one():
    for i  in range(6):
        def Tree():#ตัว - 
            del Number[i]
            del Number[i-1]
        def Four():#ตัว +
            del Number[i-2]
            n = int(Number[i-3])#ตำแหน่งตัวที่จะ +
            N = int(Number[i-4])#ตำแหน่งตัวที่จะ +
            M = n+N
            Number.append(M)#แอดตัวเข้าไปใน Number 
        def  Five():
            del Number[i-2]
            n = int(Number[i-3])#ตำแหน่งตัวที่จะ *
            N = int(Number[i-4])#ตำแหน่งตัวที่จะ *
            M = n*N
            Number.append(M)#แอดตัวเข้าไปใน Number 
        n = number[i]
        N = Number.append(n)
        test = N if n==1 else N if n==2 else Tree() if n=='-' else Four() if n=='+' else Five() if n=='d' else N
        print(i,Number)
    output = sum(Number)
    print(output)
    print('ข้อสอบที่จารเคยสั่งก่อนจะสอบ เช่น เลข 1+ตัวข้างหน้า 2ลบ ฯลฯ')
one()