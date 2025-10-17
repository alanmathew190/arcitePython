#!/usr/bin/env python
# coding: utf-8

# In[12]:


try:
    result=6/0
except ZeroDivisionError:
    print("You cant divide with zero")
else:
    print("result is : ",result)
finally:
    print("Thank you!! have a great day")



# In[17]:


fruits=["apple","orange","grapes"]
try:
    result=fruits[2]
except Exception: #Exception used to handle all types of errors
    print("There is no fruits in given index")
else: print(result)
finally:
    print("Thank you!! have a great day")


# In[19]:


try:
    age=int(input("Enter your age"))
except Exception:
    print("should be in integer numbers")
else:
    print("Your age is :",age)


# In[ ]:




