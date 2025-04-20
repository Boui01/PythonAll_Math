#def mysum(seq):
  #if len(seq) == 0 :return 0
  #return seq[0] + sum(seq[1:])

#print(mysum([]))

from functools import reduce
mysum1 = [0]
mysum = reduce(lambda x,y: x+y,\
        filter(lambda x :x if x>0 else x==0,mysum1))
print(mysum)
