import sys
string=[]
N=int(sys.stdin.readline())
for i in range(N):
    a=input()
    if a in string:
        pass
    else:
        string.append(a)
string.sort()
string.sort(key=lambda x:len(x))
for i in range(len(string)):
    print(string[i])