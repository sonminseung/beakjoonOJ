a,b=map(int,input().split())
S=set()
for i in range(a):
    p=input()
    S.add(p)
ans=0
for g in range(b):
    u=input()
    if u in S:
        ans+=1
print(ans)

