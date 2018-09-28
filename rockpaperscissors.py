import random

print("WELCOME TO LEGEND OF ALL GAMES,THE ROCK PAPER SCISSORS")

isWin = False
PlayerInput=0
while isWin == False:
    print("")
    print("Press 1 for Rock.")
    print("Press 2 for Paper.")
    print("Press 3 for Scissors.")
    while(PlayerInput==0)  :
        PlayerInput = int(input("What would you like to play?"))

    ComputerInput = random.randint(1,3)

    if (PlayerInput == 1) and (ComputerInput == 1):
        isWin = False
        print("It's a draw; you both played Rock!")
        
    if (PlayerInput == 2) and (ComputerInput == 1):
        isWin == True
        print("You win, computer played Rock!")

    if (PlayerInput == 3) and (ComputerInput == 1):
        isWin == True
        print("You lose, computer played Rock!")
        
    if (PlayerInput == 1) and (ComputerInput == 2):
        isWin = True
        print("You lose, computer played Paper!")
        
    if (PlayerInput == 2) and (ComputerInput == 2):
        isWin == False
        print("It's a draw; the computer played Paper!")

    if (PlayerInput == 3) and (ComputerInput == 2):
        isWin == True
        print("You win, computer played Paper!")
        
    if (PlayerInput == 1) and (ComputerInput == 3):
        isWin = True
        print("You win, computer played Scissors!")
        
    if (PlayerInput == 2) and (ComputerInput == 3):
        isWin == True
        print("You lose, computer played Scissors!")

    if (PlayerInput == 3) and (ComputerInput == 3):
        isWin == False
        print("It's a draw; computer played Scissors!")
    if (PlayerInput == 1) and (ComputerInput == 3):
        isWin = True
        print("You win, computer played Scissors!")
        
    if (PlayerInput == 2) and (ComputerInput == 3):
        isWin == True
        print("You lose, computer played Scissors!")

    if (PlayerInput == 3) and (ComputerInput == 3):
        isWin == False
        print("It's a draw; computer played Scissors!")
