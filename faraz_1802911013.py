a = [[2,3,4],[7,8,9],[16,17,15]]
b =[]
for i in range(len(a)):
    temp = min(a[i])
    b=b+[temp]
print(max(b))
