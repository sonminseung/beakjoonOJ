row,column=map(int,input().split())
color_row=[]
number=[]
for i in range(row):
    color_coulmn=[]
    color=input()
    for a in range(len(color)):
        color_coulmn.append(color[a])
    color_row.append(color_coulmn)
for i in range(row-7):
    for a in range(column-7):
        index1=0
        index2=0
        for u in range(i,i+8):
            for z in range(a,a+8):
                if (u+z)%2==0:
                    if color_row[u][z]!='W':
                        index1+=1
                    if color_row[u][z]!='B': 
                        index2+=1
                else:
                    if color_row[u][z]!='B':
                        index1+=1
                    if color_row[u][z]!='W': 
                        index2+=1
        number.append(min(index1,index2))
print(min(number))
    
        



