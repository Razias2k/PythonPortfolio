#!/usr/bin/env python
# coding: utf-8

# In[28]:


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26
def caesar(normal_text, shift_num, EorD):
    cipher_text = ""
    if EorD == "decode":
        shift_num *= -1
    for char in normal_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_num
            new_letter = alphabet[new_position]
            cipher_text = cipher_text + new_letter
        else:
            cipher_text += char
                
        
    print(f"You chose to {EorD} the message. The message reads: {cipher_text}")
            
caesar(text, shift, direction)


# In[ ]:




