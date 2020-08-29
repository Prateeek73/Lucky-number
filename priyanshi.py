m=int(input())
n=int(input())
l=[]
k=[]
for i in range(m):
    o=[]
    for j in range(n):
        a=int(input())
        o.append(a)
    l.append(o)
    k.append(min(o))
print(max(k))
