import random as random

possibleChoices = ["rock", "paper", "scissors"]

class Player:
    def __init__(self,playerName="Oponnent",playerChoice=random.choice(possibleChoices)):
        self.playerName = playerName
        self.playerChoice = playerChoice
    def getName(self):
        while True:
            chosenName = input("What is your name? ")
            if len(chosenName) < 1:
                print("Please enter a name that is at least one (1) character long.")
            else:
                self.playerName = chosenName
                break
    def makeChoice(self):
        while True:
            chooses = input("Choose Rock, Paper, or Scissors: ").lower()
            if chooses not in possibleChoices:
                print("That is not a valid choice. Please choose again.")
            else:
                self.playerChoice = chooses
                break
    def makeWinner(self):
        self.isWinner = True