#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

from hangman_art import logo
print(logo)

from hangman_words import word_list
display = []
randomWord = random.choice(word_list)

for blank in randomWord:
     display = display + ["_"]

game_over = False
lives = 6

while not game_over:
    
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(randomWord)):
        letter = randomWord[position]
        if letter == guess:
            display[position] = guess
            
    if guess not in randomWord:    
        print(f"You guessed {guess}. That's not in the word. You've lost a life.")
        
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You lose. The word was {randomWord}")
    
    
    print(f"{' '.join(display)}")
    if "_" not in display:
        game_over = True
        print("You win!")
    
    from hangman_art import stages
    print(stages[lives])


# In[ ]:




