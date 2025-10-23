#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Cupcake:
    def __init__(self):
        print("A cupcake is created")

cake1=Cupcake()
cake2=Cupcake()
cake3=Cupcake()

print("cake1",cake1)
print("cake2",cake2)
print("cake3",cake3)


# In[14]:


class Cupcake1:
    def __init__(self,flavour):
        self.flavour=flavour

cake11=Cupcake1("coco")
cake12=Cupcake1("vanila")
cake13=Cupcake1("pista")

print("cake1",cake11.flavour)
print("cake2",cake12.flavour)
print("cake3",cake13.flavour)


# In[22]:


class Person:
     def __init__(self,name,age):
         self.name=name
         self.age=age

alan=Person("Alan",22)
vijay=Person("Vijay",23)
ashish=Person("Ashish",21)
print(alan.name,alan.age)
print(vijay.name,vijay.age)
print(ashish.name,ashish.age)


# In[28]:


class Person:
     def __init__(self,name,age):
         self.name=name
         self.age=age
     def Introduce(self):
         print("Hi I am",self.name,"and I am",self.age,"years old")
alan=Person("Alan",22)
vijay=Person("Vijay",23)
ashish=Person("Ashish",21)

alan.Introduce()
vijay.Introduce()
ashish.Introduce()


# In[31]:


class Cars:
     def __init__(self,name,model,year):
         self.name=name
         self.model=model
         self.year=year
     def Introduce(self):
         print("This is a",self.year,self.name,self.model)
bmw=Cars("BMW","m4",2020)
city=Cars("Honda","city",2018)
thar=Cars("Mahindra","Thar",2021)

bmw.Introduce()
city.Introduce()
thar.Introduce()


# In[ ]:




