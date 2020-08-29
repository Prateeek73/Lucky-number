mat = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
arMin = []
for i in range(len(mat)):
    mini = min(mat[i])
    arMin.append(mini)
maxEle = max(arMin)
print(maxEle)
