#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

optionList = [rock, paper, scissors]
#prompts for choice and prints choice
prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors"))

if prompt >= 3 or prompt < 0:
    print("Invalid number choice. You lose.")
else:
    print(optionList[prompt])


    CPU_choice = random.randint(0,2)
    print("CPU chose: ")
    print(optionList[CPU_choice])


    if prompt == 0 and CPU_choice == 2:
        print("You win!")
    elif CPU_choice == 2 and prompt == 0:
       print("You lose!")
    elif CPU_choice > prompt:
       print("You lose!")
    elif prompt > CPU_choice:
        print("You win!")
    elif CPU_choice == prompt:
       print("It's a draw!")
    



