"""
String Lists

strings lists index

Exercise 6:
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

mystring = input("Please enter a name: ")
if mystring.lower() == mystring[::-1].lower():
    print("This name is a palindrome.")
else:
    print("This name isn't a palidrome.")