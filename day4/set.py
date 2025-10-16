#!/usr/bin/env python
# coding: utf-8

# In[1]:


mySet={1,2,3,4}
print(mySet)


# In[3]:


mySet.add(6)
print(mySet)


# In[4]:


mySet.add(4)
print(mySet)


# In[5]:


mySet.update([7,8,9])
print(mySet)


# In[6]:


mySet.remove(4)
print(mySet)


# In[8]:


mySet.discard(9) #delete an element if it exists else no error shown just ignores
mySet.discard(4) #no error shown
print(mySet)


# In[10]:


set1={1,2,3,4,5}
set2={3,4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))


# In[ ]:




