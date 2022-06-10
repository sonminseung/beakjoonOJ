M=int(input())
number=[int(x) for x in input().split()]
dic_num={i:1 for i in number}
N=int(input())
number2=[int(y) for y in input().split()]
for a in number2:
    if dic_num.get(a):
         print(1, end=' ')
    else:
         print(0, end=' ')
