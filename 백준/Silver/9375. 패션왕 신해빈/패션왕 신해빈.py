from collections import Counter
T=int(input())
for i in range(T):
    n=int(input())
    type=[]
    for a in range(n):
        wear_name,wear_type=input().split(' ')
        type.append(wear_type)

    wear_counter=Counter(type)
    cnt=1
    for key in wear_counter:
        cnt *= wear_counter[key] + 1

    print(cnt-1)        