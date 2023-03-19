choice = input("Choose Rock, Paper, or Scissors: ")
while True:
    if choice.upper() not in ["ROCK", "PAPER", "SCISSORS"]:
        print("That is not a valid choice. Please choose again.")
        choice = input("Choose Rock, Paper, or Scissors: ")
    else:
        break
print(f"You chose {choice.upper()}")