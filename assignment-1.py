#!/usr/bin/env python
# coding: utf-8

'''Assignment 1
This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.
This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.
    Parameters
    ----------
    x: int
        the integer whose factorial to return
    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line

# In[3]:


x = int(input("Enter integer whose factorial to be returned:"))
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(x))



def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9
    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.
    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line



# In[12]:


number_grade = float(input("Enter number grade to convert into a letter grade"))
def classify_grade(number_grade):
    if number_grade>=92:
        return 'A'
    elif number_grade>=86:
        return 'B+'
    elif number_grade>=80:
        return 'B'
    elif number_grade>=74:
        return 'C+'
    elif number_grade>=67:
        return 'C'
    elif number_grade>=60:
        return 'D'
    elif x>=0:
        return 'F'
print(classify_grade(x))


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.
    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line

# In[15]:


items1 = int(input("Enter number of items in the first bag:"))
weight1 = float(input("Enter the weight of each item in the first bag:"))
items2 = int(input("Enter number of items in the second bag:"))
weight2 = float(input("Enter the weight of each item in the second bag:"))


w_avg = float(((items1*weight1)+(items2*weight2))/(items1+items2))

print(w_avg)


def string_sum(string):
    '''Item 4.
    String Sum. 3 points.
    
    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.
    Parameters
    ----------
    string: str
        a string that can contain any character.
    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line

# In[17]:


string = str(input("Enter string of any characters:"))

def string_sum(string):
    sum = 0
    for x in string:
        if x.isdigit() == True:
            sum += int(x)
    return sum

print(string_sum(string))


def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.
    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum
    You may want to import the `math` library for this number.
    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate
    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line

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


def make_change(amount):
    '''Item 6.
    Make Change. 5 points.
    
    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.
    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.
    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line

# In[ ]:

i= int(input("Enter the amount, in centavos, to make change for "))

def make_change(i):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    
    if i>=100:
                a = i/100
                i %= 100

    if i>=25:
                b = i/25
                i %= 25
    
    if i>=10:
                c = i/10
                i %=10
    
    if i>=5:
                d = i/5
                i %= 5
    
    if i>0:
                e = i/1
                i = 0

    return " 1P: %i / 25C: %i / 10C: %i / 5C: %i / 1C: %i " %(a , b, c, d, e)
    
print(make_change(i))
