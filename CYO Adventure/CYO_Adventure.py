#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

decision1 = input("You approach a crossroad. Do you go left or right? ")
decision1 = decision1.lower()

if decision1 == "right":
    print("You were attacked by a group of bandits. Game over.")
else: 
    decision2 = input("You continue down the left path, and come across a river. Do you wait on a boat, or try to swim across?")
    decision2 = decision2.lower()
    
    if decision2 == "swim":
        print("You grew exhausted and drowned. Game over.")
    else: 
        decision3 = input("You wait, and a boat approaches. You take the boat and are dropped off at a set of three doors: Red, Blue, and Green.\nWhich door do you take?")
        decision3 = decision3.lower()
        
        if decision3 == "red":
            print("As you reach for the handle, an explosion erupts from the door, killing you instantly. Game over.")
        elif decision3 == "blue":
            print("You open the door to find a group of angry silithids that attack you immediately. Game over.")
        else:
            print("You open the green door to a room with enough riches for 10 lifetimes. You Win!")
        
        
    
    
    


# In[ ]:




