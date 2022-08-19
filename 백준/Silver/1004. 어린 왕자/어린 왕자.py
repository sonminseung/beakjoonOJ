import math
T=int(input())
entry_exit=0
for i in range(T):
    entry_exit=0
    x1,y1,x2,y2=list(map(int,input().split(' ')))
    count=int(input())
    for _ in range(count):
        cx,cy,r=map(int,input().split(' '))
        dis1=math.sqrt(abs(x1-cx)**2+abs(y1-cy)**2)
        dis2=math.sqrt(abs(x2-cx)**2+abs(y2-cy)**2)
        if dis1<r and dis2>r:
            entry_exit+=1
        elif dis1>r and dis2<r:
            entry_exit+=1
    print(entry_exit)
        
