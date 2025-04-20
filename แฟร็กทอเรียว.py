def factorail(n):

     f = 1

     for i in range(1,n+1):
        f = (f*i)
     return f

def factorail2(n):
     f2 = 1
     
     for i in range(1,n+1):
        f2 = (f2*i)
     return f2

factorail3 = factorail(6)/factorail2(4)

print(factorail3)
