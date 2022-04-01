#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Fibonacci Sequence

a=int(input("No. of terms: "))
x=0
y=1
if a<=0:
    print(x)
else:
    print(x,y,end=' ')
    for i in range(2,a):
        z=x+y
        print(z,end=' ')
        x=y
        y=z


# In[ ]:





# In[ ]:




