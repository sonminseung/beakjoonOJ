a,b=map(int, input().split())
count=2
counts=[]
result1=1
while(1):
    if a%count==0 and b%count==0:
        counts.append(count)
        a=a/count
        b=b/count
        count=2
    else:
        count+=1
        if count>a or count>b:
            break
for i in counts:
    result1*=i
result2=result1*a*b
print(int(result1))
print(int(result2))

