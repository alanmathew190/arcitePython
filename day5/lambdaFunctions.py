#!/usr/bin/env python
# coding: utf-8

# In[9]:


square=lambda x:x*x #single argument
print(square(10))


# In[8]:


tot=lambda x,y:x+y #more than one argument
print(tot(4,5))


# In[7]:


total=lambda *args:sum(args) #countless argument
print(total(3,4,5,6,7,8))


# In[11]:


#map using lambda
nums=[1,2,3,4,5]
squared= map(lambda x:x*x,nums)
print(list(squared))


# In[14]:


#filter using lambda
nums=[1,2,3,4,5]
even= filter(lambda x:x%2==0,nums)
print(list(even))


# In[19]:


#reduce using lambda
from functools import reduce 
nums=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,nums)
print(product)


# In[ ]:

nums=[1,2,3,4,5,6]
square=map(lambda x:x*x,nums)
even=filter(lambda x:x%2==0,square)
print(list(even))


# %%
