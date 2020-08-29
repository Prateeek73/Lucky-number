r=int(input())
c=int(input())
arr=[]
Max=[]
for i in range(r):
    Min=[]
    for j in range(c): 
         Min.append(int(input()))
    matrix.append(Min)
    Max.append(min(Min))
print(max(Max))
