"""
Rock Paper Scissors

Exercise 8:

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
gameOn = True

while gameOn == True:
    #Get input from the users
    playerOne = input(" Player 1, choose Rock,Paper, or Scissors: ")
    playerTwo = input(" Player 2, choose Rock,Paper, or Scissors: ")

    #Setting up the logic of the game
    if playerOne.lower() == "rock" and playerTwo.lower() == "scissor":
        print("Player One wins!")
    elif playerOne.lower() == "paper" and playerTwo.lower() == "rock":
        print("Player One wins!")
    elif playerOne.lower() == "scissors" and playerTwo.lower() == "paper":
        print("Player One wins!")
    elif playerOne.lower() == playerTwo.lower():
        print("This game is a tie")
    else:
        print("Player 2 wins!")
        
    #Checking to see if the game should continue    
    keepPlaying = input("Would you like to keep playing? y/n: ")

    if keepPlaying.lower() == 'y':
        gameOn = True
    else:
        gameOn = False
