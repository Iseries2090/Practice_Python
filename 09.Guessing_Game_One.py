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
userGuess = 0
num = random.randint(1,10)
gameOn = True

while gameOn == True:
    

    #Enable some error handling to make sure the user picks 1-10
    try:
        guessNum = int(input("Pick a number 1-10: "))
    except:
        print("That is not a valid option. Try again.")
    else:
        if guessNum > 10 or guessNum < 1:
            print("Please pick a number between 1-10.")
        else:
            continue

    #Conditional statements
    if guessNum < num:
        print("You're guess is too low. Try again.")
        userGuess += 1
    elif guessNum > num:
        print("You're guess is too high. Try again.")
        userGuess += 1
    else:
        print("That is correct!")
    
    #final print statments and check to see if the game should continue.
    print("It took {} guess(es).".format(userGuess))
    userInput = input("Do you wish to continue?  Type Yes to continue or exit to quit: ")
    
    if userInput.lower() == 'y':
        gameOn == True

        #reset the variables for new game
        userGuess = 0
        num = random.randint(1,10)
    else:
        gameOn == False
    