from math import factorial
N=int(input())
T=factorial(N)
count=0
T=list(map(int,str(T)))
if len(T)==1:
    print(0)
else:
    while 1:
        if len(T)==0:
            break
        if T[-1]==0:
            count+=1
            T.pop()
            if T[-1]!=0:
                break
        else:  
            T.pop()
    print(count)
