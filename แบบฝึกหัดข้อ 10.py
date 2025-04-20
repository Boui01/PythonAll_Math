from collections import defaultdict

def pmf(data):
    f_count = defaultdict(int)
    for i in data:
        f_count[i]+=1

    return[ (k,v/len(data))for k,v in f_count.items()]
data = [1,2,3,4,5,5]
print(pmf(data))
