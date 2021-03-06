"""
Fibonacci

Exercise 13:

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""

def create_fibonnacci(num):
    #Create an empty list to store the values
    result = []

    #add the first two values into the list
    result.append(1)
    result.append(1)

    #starting a counting loop to go up to the user input number of sequences
    for x in range (1,num):
        nextNum = result[x-1]
        nextNum += result[x]
        result.append(nextNum)
    return result

#Asking the user for the number of sequences
y = int(input("How many numbers in the fibonnacci sequence: "))

print(create_fibonnacci(y))