import sys
number=[]
n=sys.stdin.readline()
number=list(n)
del number[len(number)-1]
number.sort()
for i in range(len(number)-1,-1,-1):
    print(number[i],end='')