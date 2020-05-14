"""
List Ends

Exercise 12:

Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and
last elements of the given list. For practice, write this code inside a function.
"""
a = [5, 10, 15, 20, 25]

def get_num(num):
    result = []
    result.append(num[0])
    result.append(num[-1])
    return result

print(get_num(a))
