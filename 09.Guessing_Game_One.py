"""
Guessing Game One   

Exercise 9:

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high,
or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

#Set up the variables
import random
randnum = random.randint(1,11)
game_on = True

while True:
    while True:
        try:
            usernum = int(input("Please input a number between 1 and 10: "))
        except ValueError:
            print("That is not a number, please try again")
        else:
            if usernum > 10 or usernum < 1:
                print("That is not in the range, please try again")
            else:
                break
    if usernum > randnum:
        print("{} is too high, please try again".format(usernum))
    elif usernum < randnum:
        print("{} is too low, please try again.".format(usernum))
    else:
        print("Congrats, {} is the right answer!".format(usernum))
        exit()
    