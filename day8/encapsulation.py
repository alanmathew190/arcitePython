#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Encapsulation

class Cupcake:
    def __init__(self,flavour):
        self.__flavour=flavour

    def get_flavour(self):
        return self.__flavour

    def set_flavour(self,new_flavour):
        self.__flavour=new_flavour



cake1=Cupcake("coco")
print(cake1.get_flavour())
cake1.set_flavour("vanila")
print(cake1.get_flavour())


# In[ ]:




