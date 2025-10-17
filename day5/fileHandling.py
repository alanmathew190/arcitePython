#!/usr/bin/env python
# coding: utf-8

# In[4]:


with open("C:/New folder/myfile2.txt","w") as file:
    file.write("Hello, I Am learning python")


# In[1]:


with open("C:/New folder/myfile2.txt","r") as file:
    content=file.read()
    print(content)


# In[1]:


with open("C:/New folder/myfile2.txt","a") as file:
    file.write("This is another line \n")


# In[3]:


with open("C:/New folder/myfile2.txt","r")as source:
    with open("C:/New folder/myfile2.txt","w")as target:
        content=source.read()
        print(content)
        target.write(content)


# In[ ]:




