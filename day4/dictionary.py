#!/usr/bin/env python
# coding: utf-8

# In[1]:


person={"name":"Alice","age":25,}
print(person)


# In[2]:


print(person["name"])


# In[3]:


person.keys()


# In[5]:


person.values()


# In[6]:


age=person.pop("age")
print(age)
print(person)


# In[8]:


person.update({"age":25,"gender":"female"})
print(person)


# In[10]:


person.clear()
print(person)


# In[ ]:




