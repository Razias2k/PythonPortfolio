#!/usr/bin/env python
# coding: utf-8

# In[46]:


weight = input("Weight: ")
decision = input("(K)g or (L)bs: ")

weight_float = float(weight)

if (decision.upper() == "L"):
    (weightKG) = weight_float / 2.205
    
    KG_str = str(weightKG)
    print("Weight in Kg : " + KG_str)

elif (decision.upper() == "K"):
        weightLBS = (weight_float * 2.205)
        
        LBS_str = str(weightLBS)
        print("Weight in Kg : " + LBS_str)
    
else:
    print("That is not a valid input")
    

    

