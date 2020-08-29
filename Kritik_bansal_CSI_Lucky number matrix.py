#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input())
m=int(input())
matrix=[]
t=[]
for i in range(n):
    a=[]
    for j in range(m): 
         a.append(int(input()))
    matrix.append(a)
    t.append(min(a))
print(max(t))


# In[ ]:




