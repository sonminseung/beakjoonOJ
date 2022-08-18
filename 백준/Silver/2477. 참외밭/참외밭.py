K=int(input())
length=[]
for _ in range(6):
    a,b=map(int,input().split(" "))
    length.append([a,b])
width=0
height=0
h_width=0
h_height=0

for i in range(len(length)):
    if length[i][0]==1 or length[i][0]==2:
        if width<length[i][1]:
            width=length[i][1]
            h_width=i
for q in range(len(length)):
    if length[q][0]==3 or length[q][0]==4:    
        if height<length[q][1]:
                height=length[q][1]
                h_height=q
area=height*width
sub_box1=length[(h_width+3)%6][1]
sub_box2=length[(h_height+3)%6][1]
sub_area=sub_box1*sub_box2
area=area-sub_area
print(area*K)

