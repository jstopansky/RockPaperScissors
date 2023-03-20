import random as random

possibleChoices = ["rock", "paper", "scissors"]

while True:
    playerChoice = input("Choose Rock, Paper, or Scissors: ").lower()
    if playerChoice not in possibleChoices:
        print("That is not a valid choice. Please choose again.")
    else:
        break

opponentChoice = random.choice(possibleChoices)

print(f"You chose {playerChoice}")
print(f"Your opponent chose {opponentChoice}")

if playerChoice == opponentChoice:
    print("It's a tie!")
elif playerChoice == "rock":
    if opponentChoice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif playerChoice == "paper":
    if opponentChoice == "scissors":
        print("Scissors cuts paper. You lose.")
    else:
        print("Paper covers rock. You win!")
elif playerChoice == "scissors":
    if opponentChoice == "rock":
        print("Rock crushes scissors. You lose.")
    else:
        print("Scissors cuts paper. You win!")
