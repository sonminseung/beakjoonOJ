T=int(input())
r=list(map(int,input().split(" ")))
for _ in range(1,T):
    count=2
    r1=r[0]
    r2=r[_]
    while 1:
        if r1%count==0 and r2%count==0:
            r1=r1/count
            r2=r2/count
            count=2
        else:
            count+=1
            if r1<count or r2<count:
                break
        r1=int(r1)
        r2=int(r2)
    print(str(r1)+'/'+str(r2))