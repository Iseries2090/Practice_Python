"""
Check Primality Functions   

Exercise 11:

Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you.
"""



def get_primality(num):
    count = 0
    if num > 1:
        for x in range (1,num):
            if num % x == 0:
                count += 1
    if count > 1:
        print("{}, is not a prime number".format(num))
    else:
        print("{}, is a prime number.".format(num))


num = int(input("Please enter a number to check if its a prime number: "))

get_primality(num)