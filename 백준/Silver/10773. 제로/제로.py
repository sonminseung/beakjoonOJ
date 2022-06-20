import sys
K=int(sys.stdin.readline())
S=[]
result=0
for a in range(K):
    i=int(sys.stdin.readline())
    if i==0:
        S.pop()
    else:
        S.append(i)
for a in S:
    result+=a
print(result)


