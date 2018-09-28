import random

print("Hello! Welcome to the Rock Paper Scissors Program!")

isWin = False

while isWin == False:
    print("")
    print("Press 1 for Rock.")
    print("Press 2 for Paper.")
    print("Press 3 for Scissors.")

    UserInput = int(input("What would you like to play?"))
    ComputerInput = random.randint(1,3)

    if (UserInput == 1) and (ComputerInput == 1):
        isWin = False
        print("It's a draw; you both played Rock!")
        
    if (UserInput == 2) and (ComputerInput == 1):
        isWin == True
        print("You win! The computer played Rock!")

    if (UserInput == 3) and (ComputerInput == 1):
        isWin == True
        print("You lose! The computer played Rock!")
        
    if (UserInput == 1) and (ComputerInput == 2):
        isWin = True
        print("You lose! The computer played Paper!")
        
    if (UserInput == 2) and (ComputerInput == 2):
        isWin == False
        print("It's a draw; the computer played Paper!")

    if (UserInput == 3) and (ComputerInput == 2):
        isWin == True
        print("You win! The computer played Paper!")
        
    if (UserInput == 1) and (ComputerInput == 3):
        isWin = True
        print("You win! The computer played Scissors!")
        
    if (UserInput == 2) and (ComputerInput == 3):
        isWin == True
        print("You lose! The computer played Scissors!")

    if (UserInput == 3) and (ComputerInput == 3):
        isWin == False
        print("It's a draw; the computer played Scissors!")