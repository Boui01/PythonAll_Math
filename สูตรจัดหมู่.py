def factorail(n):

     f = 1

     for i in range(1,n+1):
        f = (f*i)
     return f
def factorail2(n,r):

    f2 = 1
    N = n-r
    for i in range(1,N+1):
        f2 = (f2*i)
    return f2
def factorail3(r):

    f2 = 1

    for i in range(1,r+1):
        f2 = (f2*i)
    return f2

ft1 = factorail(15)#n
ft2 = factorail2(15,10)#n-r
ft3 = factorail3(10)#r

Ft1 = '1!'if ft1==1 else '2!' if ft1==2 else '3!'if ft1==6 else '4!'\
      if ft1==24 else '5!' if ft1==120 else '6!' if ft1==720 else '7!'\
      if ft1==5040 else '8!' if ft1==40320 else '9!' if ft1==362880 else '10!'\
      if ft1==3628800 else '11!' if ft1==39916800 else '12!' if ft1==479001600\
      else '13!' if ft1==6227020800 else '14!' if ft1==87178291200 else '15!'

Ft2 = '1!'if ft2==1 else '2!' if ft2==2 else '3!'if ft2==6 else '4!'\
      if ft2==24 else '5!' if ft2==120 else '6!' if ft2==720 else '7!'\
      if ft2==5040 else '8!' if ft2==40320 else '9!' if ft2==362880 else '10!'\
      if ft2==3628800 else '11!' if ft2==39916800 else '12!' if ft2==479001600\
      else '13!' if ft2==6227020800 else '14!' if ft2==87178291200 else '15!'

Ft3 = '1!'if ft3==1 else '2!' if ft3==2 else '3!'if ft3==6 else '4!'\
      if ft3==24 else '5!' if ft3==120 else '6!' if ft3==720 else '7!'\
      if ft3==5040 else '8!' if ft3==40320 else '9!' if ft3==362880 else '10!'\
      if ft3==3628800 else '11!' if ft3==39916800 else '12!' if ft3==479001600\
      else '13!' if ft3==6227020800 else '14!' if ft3==87178291200 else '15!'


factorail4 = ft1/(ft2 * ft3)

print('      ',Ft1,'             ',Ft1)
print('-----------------',' = ','-------',' = ',factorail4)
print(Ft3,'(',Ft1,'-',Ft3,')','    ',Ft3,Ft2)

