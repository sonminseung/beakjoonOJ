def hanoi(num,From,to,other):
    if num==1:
        print('%d %d' %(From, to))
        return
    hanoi(num-1,From,other,to)
    print('%d %d' %(From ,to))
    hanoi(num-1,other,to,From)
a=int(input())
print(2**a-1)
hanoi(a,1,3,2)