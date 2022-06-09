all_num=set(range(1,10001))
num=set()
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    num.add(i)
self_numlist=sorted(all_num-num)
for a in self_numlist:
    print(a)