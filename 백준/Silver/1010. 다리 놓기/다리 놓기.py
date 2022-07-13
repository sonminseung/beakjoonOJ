import math 
T=int(input())
for _ in range(T):
    a,b=map(int,input().split(" "))
    print(math.factorial(b)//(math.factorial(b-a)*math.factorial(a)))

