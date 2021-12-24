#!/usr/bin/env python
# coding: utf-8

# In[19]:


from collections import deque
def solution(priorities : list, location : int) -> int:
    answer=0
    leng=len(priorities)
    ans_list= deque(list(range(leng)))
    ordered_list=[]
    priorities=deque(priorities)
    
    while len(ans_list)!=0:
        if priorities[0]<max(priorities):
            priorities.append(priorities.popleft())
            ans_list.append(ans_list.popleft())

        else:
            ordered_list.append(ans_list.popleft())
            priorities.popleft()
    answer= ordered_list.index(location)+1
    return answer

