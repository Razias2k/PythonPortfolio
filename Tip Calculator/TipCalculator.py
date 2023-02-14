#!/usr/bin/env python
# coding: utf-8

# In[15]:


print("Welcome to your personal tip calculator.")

totalBill = input("What was the total bill? ")
totalPeople = input("How many people are splitting the bill? ")
percent_Tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

percent_Tip_Conversion = float(percent_Tip) / 100

splitTotal = float(totalBill) / int(totalPeople)

## print(splitTotal)

tipShare = float(splitTotal) * float(percent_Tip_Conversion)

print("Each person should tip", "${:.2f}".format(tipShare) )


# In[ ]:




