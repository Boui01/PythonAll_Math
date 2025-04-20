num1 = set([1,2,2,1])
num2 = [2,2]
num3 = num1.intersection(num2)

num4 = [(i,i) for i in num3 if i==2]
print(num4)
    

