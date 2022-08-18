import math
T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split(" "))
    distance=math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)
    if distance==0 and r1==r2:
        print(-1)
    elif abs(r1-r2)==distance or r1+r2==distance:
        print(1)
    elif abs(r1-r2)<distance<r1+r2:
        print(2)
    else:
        print(0)