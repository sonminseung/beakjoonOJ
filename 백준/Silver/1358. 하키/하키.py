import math
W,H,X,Y,P=map(int,input().split(' '))
count=0
for i in range(P):
    x1,y1=map(int,input().split(' '))
    dis1=math.sqrt(abs(x1-X)**2+abs(y1-(Y+H/2))**2)
    dis2=math.sqrt(abs(x1-(W+X))**2+abs(y1-(Y+H/2))**2)
    if X<=x1<=X+W and Y<=y1<=Y+H:
        count+=1
    elif dis1<=H/2 or dis2<=H/2:
        count+=1
print(count)

    