# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:39:46 2017

@author: Jacques Menard
"""

import random
# Assumption: listOfList is a list of 0 or more non-empty lists
#

#My implementation of randChoices with just the 2 lines
#applies random.choice() to every sublist of the input
def randChoices(listOfLists):
    return [random.choice(sublist) for sublist in listOfLists]

# creates a list of all the numbers from 0 to max number then checks if digit is a digit of each element
# by converting them both to strings and seeing if the element contains the digit, creating a new list that matches that criteria.
# returns the length of that new list
def howManyNumsWithDigit(maxNumber, digit):
    return (len([i for i in range(0,maxNumber+1) if(str(digit) in str(i)) ]))