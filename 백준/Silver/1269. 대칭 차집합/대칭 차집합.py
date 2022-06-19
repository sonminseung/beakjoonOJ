a,b=map(int,input().split())
A=set(input().split())
B=set(input().split())
N=A-B
M=B-A
print(len(M)+len(N))