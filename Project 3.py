#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Positive Numbers in the given list
l=list(eval(input("Enter the numbers needed seperated with commas: ")))
print('Input numbers are: ',l)
o=[]
for i in l:
    if i>0:
        o.append(i)
print('Positive Integers are: ',o)


# In[ ]:




