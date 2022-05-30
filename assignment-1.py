#!/usr/bin/env python
# coding: utf-8

# In[3]:


x = int(input("Enter integer whose factorial to be returned:"))
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(x))


# In[12]:


x = float(input("Enter number grade to convert into a letter grade"))
def lettergrade(x):
    if x>=92:
        return 'A'
    elif x>=86:
        return 'B+'
    elif x>=80:
        return 'B'
    elif x>=74:
        return 'C+'
    elif x>=67:
        return 'C'
    elif x>=60:
        return 'D'
    elif x>=0:
        return 'F'
print(lettergrade(x))


# In[15]:


items1 = int(input("Enter number of items in the first bag:"))
weight1 = float(input("Enter the weight of each item in the first bag:"))
items2 = int(input("Enter number of items in the second bag:"))
weight2 = float(input("Enter the weight of each item in the second bag:"))

w_avg = float(((items1*weight1)+(items2*weight2))/(items1+items2))

print(w_avg)


# In[17]:


string = str(input("Enter string of any characters:"))

def string_sum(str):
    sum = 0
    for x in str:
        if x.isdigit() == True:
            sum += int(x)
    return sum

print(string_sum(string))


# In[19]:


x1 = float(input("Enter the first x-coordinate:"))
y1 = float(input("Enter the first y-coordinate:"))
x2 = float(input("Enter the second x-coordinate:"))
y2 = float(input("Enter the second y-coordinate:"))

xsq = (x2-x1)**2
ysq = (y2-y1)**2

import math

dist = float(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))

print(dist)


# In[ ]:


amount = float(input("Enter amount to make change for:"))

calculate_25C = amount//25
print ("25C:",str(calculate_25C))
amount = amount%25

calculate_10C = amount//10
print ("10C:",str(calculate_10C))
amount = amount%10


# In[90]:


a = float(input("Enter amount to make change for:"))

P1 = int(a)

print("1P:",P1)

b = round(a-(a//1),2)

print(b)

b_cents =int((b)*100)

print(b_cents)

C25 = int(b_cents//25)

print("25C:", C25)

b_cents-=C25*25

C10 = int(b_cents//10)
print("10C:", C10)

b_cents-=C10*10

C5 = int(b_cents//5)
print("5C:", C5)

b_cents-=C5*5

print("1C:",b_cents)

