"""
Odd Or Even 
input if types int equality comparison numbers mod
Again, the exercise comes first 
(with a few extras if you want the extra challenge or want to spend more time), 
followed by a discussion. Enjoy!

Exercise 2:
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(input("Enter a number: "))
if num % 4 == 0:
    print("{} is a multiple of 4.".format(num))
elif num % 2 == 0:
    print("{} is an even number.".format(num))
else:
    print("{} is an odd number.".format(num))

##Extra
#num = int(input("Enter a number: "))
#check = int(input("Enter a number to check by: "))
#if num % check == 0:
#    print("{} is divided by {} evenly".format(num,check))
#else:
#   print("{} is not divided by {} evenly".format(num,check))