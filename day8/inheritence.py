#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Cupcake:
    def __init__(self,flavour):
        self.flavour=flavour
    def describe(self):
        print(f"This is a {self.flavour} flavoured cupcake")

class ChocolateCupcake(Cupcake):
    def add_topping(self):
        print("Adding Chocolate chips on top")

class VanilaCupcake(Cupcake):
    def add_topping(self):
        print("Adding vanila toppings on top")

choco=ChocolateCupcake("chocolate")
vanila=VanilaCupcake("vanila")


choco.describe()
choco.add_topping()
vanila.describe()
vanila.add_topping()


# In[ ]:




