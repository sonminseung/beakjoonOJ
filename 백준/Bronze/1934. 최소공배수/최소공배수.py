T=int(input())
for i in range(T):
    a,b=map(int, input().split(" "))
    A,B=a,b
    if b>a:
        a,b=b,a
    while b!=0:
        a=a%b
        a,b=b,a
    print(A*B//a)
