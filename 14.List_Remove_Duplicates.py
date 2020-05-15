"""
List Remove Duplicates

Exercise 14:

Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list,
and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""
import random

#Created a function to generate a random list of numbers and return a list
def create_list():
    result = []
    randInt = random.randint(1,15)
    for i in range(0,randInt+1):
        n = random.randint(1,20)
        result.append(n)
    return result

#Created a function to take in a random list of numbers and remove duplicates and return a list
def remove_duplicate(elem):
    result = elem
    return list(set(result))

#print the results
print(remove_duplicate(create_list()))