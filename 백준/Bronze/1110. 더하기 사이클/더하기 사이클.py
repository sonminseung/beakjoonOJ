T=input()
U=int(T)
count=0
while True:
    if int(T)<10:
        T=T[-1]+T[-1]
        count+=1
        if int(T)==U:
            break
    else:
        A=int(T[0])+int(T[1])
        T=T[1]+str(A)[-1]
        count+=1
        if int(T)==U:
            break
print(count)