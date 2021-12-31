#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter

def solution(n, lost, reserve):

    stu = dict()
    for i in range(1, n+1):
        stu[i] = 1
        
    for i in lost:
        stu[i] = stu.get(i)-1
        
    for i in reserve:
        stu[i] = stu.get(i)+1
        
    for k, v in stu.items():
        if v==0:
            if k==1 and stu[k+1]==2:
                        stu[k+1]=stu.get(k+1)-1
                        stu[k]=stu.get(k)+1


            elif k!=1 and k!=n:
                    if stu[k-1]==2:
                        stu[k-1]=stu.get(k-1)-1
                        stu[k]=stu.get(k)+1

                    elif stu[k+1]==2:
                        stu[k+1]=stu.get(k+1)-1
                        stu[k]=stu.get(k)+1


            elif k==n and stu[k-1]==2:
                        stu[k-1]=stu.get(k-1)-1
                        stu[k]=stu.get(k)+1
    stu=Counter(stu.values())
    return n-stu[0]

