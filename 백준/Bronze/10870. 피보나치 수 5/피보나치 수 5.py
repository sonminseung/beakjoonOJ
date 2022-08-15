number=[0,1]
a=int(input())
for i in range(2,a+1):
    number.append(0)
    number[i]=number[i-1]+number[i-2]

print(number[a])