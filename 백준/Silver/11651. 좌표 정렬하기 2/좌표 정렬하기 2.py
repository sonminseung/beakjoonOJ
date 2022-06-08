import sys
xy=[]
zero=[]
N=int(sys.stdin.readline())
for i in range(N):
    i,z=map(int,input().split())
    xy.append([i,z])
xy.sort(key=lambda x:(x[1],x[0]))

for i,j in xy:
    print(i,j)
    