import random

"""
Game Description:
-> Options:
1) snake 
2) water 
3) gun
-> Rules:
- snake beats water
- water beats gun
- gun beats snake
"""

optionsUser = {
    "snake": 1,
    "water": 2,
    "gun": 3
}

optionsComp = {
    1: "snake",
    2: "water",
    3: "gun"
}

# Game loop
while True:
    choice = input("Enter 1 to start and 0 to end game: ")
    
    if choice == "0":
        print("Game Over!")
        break  # Exit the loop

    userChoice = input("Enter your option (snake/water/gun): ").strip().lower()
    
    if userChoice not in optionsUser:
        print("Invalid input! Please choose from snake, water, or gun.")
        continue  # Restart loop for valid input

    computerChoice = random.randint(1, 3)
    computerMove = optionsComp[computerChoice]
    userMove = userChoice

    print(f"Computer chose {computerMove}")

    # Compare choices
    if optionsUser[userMove] == computerChoice:
        print("It's a tie!")
    elif (userMove == "snake" and computerMove == "water") or \
         (userMove == "water" and computerMove == "gun") or \
         (userMove == "gun" and computerMove == "snake"):
        print("You won!!")
    else:
        print("Computer won!!")
