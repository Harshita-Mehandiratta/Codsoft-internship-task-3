#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task 3 password generator
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create an empty list to store password characters
password_list = []

# Generate random letters for the password
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Generate random symbols for the password
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Generate random numbers for the password
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password characters to make it random
random.shuffle(password_list)

# Convert the list of characters into a string
password = ''.join(password_list)

# Print the generated password
print(f"Your generated password is: {password}")


# In[ ]:




