"""
List Overlap Comprehensions

Exercise 10:

This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates). Make sure your program works on two lists of
different sizes. 
"""
import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#setting up variables
a = []
b = []
num_a = random.randint(4,10)
num_b = random.randint(4,10)

#Generating two random lists
for i in range(0,num_a):
    rand_a = random.randint(1,10)
    a.append(rand_a)
for i in range (0,num_b):
    rand_b = random.randint(1,10)
    b.append(rand_b)

#Setting up a function to take in two lists and return common numbers
def get_common(a,b):
    result = []
    for x in a:
        for elem in b:
            if elem == x:
                result.append(x)
    return set(result)
print("{} this is list A".format(a))
print("{} this is list B".format(b))
print("The common numbers from list a and list b are {}".format(get_common(a,b)))