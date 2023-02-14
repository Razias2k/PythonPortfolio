#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random



#This program generates a random password and stores it into a text file with a title for convenience.


print("Personal Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_1234567890'

title = input("What website is your password for? ")

length = input("How many characters would you like your password to be? ")

length = int(length)

password = ""

for char in range(length):
    password = password + random.choice(chars)
    
file = open("passwords.txt", "a")
file.write("Site Name: " + title + "\n" + "Password: "+ password + "\n" + "\n")
file.close

print("Password successfully added to folder. Close this program to view file.")

