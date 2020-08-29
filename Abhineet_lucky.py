#Note : the program is not generalized yet, only for matrices with 3 rows and columns

import numpy as np
arr=np.array([[3,7,8],[9,11,13],[15,16,17]])
print(arr)
l=arr[0]
l.sort()
l

m=arr[1]
m.sort()
m

n=arr[2]
n.sort()
n

for i in range(3):
    if(l[i]>m[i] and l[i]>n[i]):
        x=l
    elif(m[i]>l[i] and m[i]>n[i]):
        x=m
    else:
        x=n

        
print(x[0])
