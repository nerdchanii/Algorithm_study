#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(input_list : list) -> int:
    dasom=input_list[0] 
    compe=input_list[1:N]
    compe=sorted(compe,reverse=True)
    cnt=0
    
    if N==1:
        print(cnt)
    
    else:
        while dasom<=compe[0]:
            dasom+=1
            compe[0]-=1
            compe=sorted(compe,reverse=True)
            cnt+=1
    
        print(cnt)

        
if __name__=='__main__':
    
    N=int(input())
    vote_list=[]
    
    for i in range(N):
        vote_list.append(int(input()))
    
    solve(vote_list)

