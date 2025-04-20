scores = [[6241,10,20,30],[551846,70,10,10],[56514,10,30,20]]
p = [sum(i[1:len(i)])for i in scores]
for I in range(3):
    u = p[I]
    grade = 'A' if u>= 80 else 'B' if u>=70 else'C' if u >=60 \
            else 'D' if u >=50  else'F'   
    print(u,grade)
    
