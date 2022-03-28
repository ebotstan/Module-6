#!/usr/bin/env python
# coding: utf-8

# 1. Round 4.5667 to the nearest hundreth using a build-in function, round().

# In[1]:


x = 4.5667
print(round(x, 2))


# 2. Convert "657" to an integer data type

# In[6]:


y = "657"
x = int("657")
print(x)
print(type(x))


# 3.
# Write a program to get two numbers from a user. Then, create a secret code where a code consists of 6 numbers and each number is randomly generated number between two numbers from a user. 

# In[18]:


import random as randno
first_no = int(input("Enter a first number: "))
second_no = int(input("Enter a second number: "))
firstcode = randno.randint(first_no, second_no)
secondcode = randno.randint(first_no, second_no)
thirdcode = randno.randint(first_no, second_no)
fourthcode = randno.randint(first_no, second_no)
fifthcode = randno.randint(first_no, second_no)
sixthcode = randno.randint(first_no, second_no)
code = (firstcode, secondcode, thirdcode, fourthcode, fifthcode, sixthcode)
newcode = []
for item in code:
    print(item)
    newcode.append(item)

print(f" Your secret code is {newcode}.")


# 4.
# Write a program to center align below text where number of characters per line is 40:
# 
#     Hickory, dickory, dock,
#     The mouse ran up the clock.
#     The clock struck one,
#     The mouse ran down,
#     Hickory, dickory, dock
# 
# <b>Do not use string's center method! </b>

# In[26]:


line1 = "Hickory, dickory, dock,"
line2 = "The mouse ran up the clock."
line3 = "The clock struck one,"
line4 = "The mouse ran down,"
line5 = "Hickory, dickory, dock"

print("Center aligned (width 40) :"+"{:^40}".format(line1))
print("Center aligned (width 40) :"+"{:^40}".format(line2))
print("Center aligned (width 40) :"+"{:^40}".format(line3))
print("Center aligned (width 40) :"+"{:^40}".format(line4))
print("Center aligned (width 40) :"+"{:^40}".format(line5))


# 5. Write a function to calculate the miles per gallon.
# Get a miles driven and gallons used from a user and call your function to calculate the miles per gallon. 

# In[22]:


def miles_per_gallon(miles, gallons):
    mpg = miles / gallons
    mpg = "{:.2f}".format(mpg)
    return mpg

total_miles = float(input("Enter total miles: "))
gallons_used = float(input("Enter gallons of gas used: "))

mpg = miles_per_gallon(total_miles, gallons_used)

# Display the result
print(f"Your total miles per Gallon: {mpg}")


# In[ ]:




