#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Welcome")
name = str(input("Enter Student Name :"))
std = int(input("Standard: "))
div = str(input("Division: "))
roll = int(input("Roll No. :"))
# Input marks from student
print("Enter Marks in 50")
phy = int(input("Physics : "))
chem = int(input("Chemistry : "))
math = int(input("Mathematics : "))
# percentage marks
print("Your Percentage Score")
phypercent = str((phy/50)*100)
chempercent = str((chem/50)*100)
mathpercent = str((math/50)*100)
print("Physics : " + phypercent +"\n" + "Chemistry : " + chempercent + "\n" + "Mathematics : " + mathpercent)


# In[ ]:




