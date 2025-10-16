#!/usr/bin/env python
# coding: utf-8

# In[1]:


def multiple(a,b):
    return a*b
multiple(4,5)


# In[3]:


def greet():
    print("Hello")
    print("How are you?")
    print("Good Day??")
greet()
greet()


# In[8]:


def greets(name):
    print(f"Hi {name}")

greets("Alan")


# In[10]:


def sum(a,b):
    c=a+b
    print(f"Sum is :{c}")
sum(4,5)


# In[13]:


def mult(a,b):
    c=a*b
    print(f"multiple of {a} and {b} is {c}")
mult(4,5)


# In[17]:


#Type of Arguments
#positional arguments
#Keyword Arguments
#Default arguments 
#variable length positional arguments
#variable length keyword Arguments

#positional arguments
def greets(name,age):
    print(f"hi {age} you are {name} years old")
greets("Alan",22)


# In[18]:


#Keyword Arguments

def greets(name="Alan",age=22):
    print(f"hi {name} you are {age} years old")
greets()


# In[24]:


#Keyword Arguments

def greet(name,age=22): #age is default here
    print(f"hi {name} you are {age} years old")
greet("Alan")
greet("Alan",25)


# In[1]:


#variable length positional arguments

def total(*args):
    print(sum(args))
total(4,5,2,3,4)


# In[7]:


#variable length keyword Arguments

def person(**kwargs):
    print(kwargs)
person(name="Alan",age=22,gender="male")


# In[ ]:




