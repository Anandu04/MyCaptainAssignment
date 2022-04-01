#!/usr/bin/env python
# coding: utf-8

# In[4]:


#most frequent
def most_frequent(word):
    d={}
    for key in word:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    d=dict(sorted(d.items(),key=lambda key:key[1],reverse=True))
    print(d)
most_frequent("Mississippi")


# In[ ]:




