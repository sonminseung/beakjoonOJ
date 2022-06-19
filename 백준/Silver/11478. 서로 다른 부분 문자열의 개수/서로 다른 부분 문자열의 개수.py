S=input()
S1=set()
for i in range(0,len(S)):
    for a in range(i,len(S)):
        tmp=S[i:a+1]
        S1.add(tmp)
print(len(S1))