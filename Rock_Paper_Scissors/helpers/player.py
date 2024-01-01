import random as random

possible_choices = ["rock", "paper", "scissors"]

class Player:
    def __init__(self,player_name="Oponnent",player_choice=random.choice(possible_choices)):
        self.player_name = player_name
        self.player_choice = player_choice
    def get_name(self):
        while True:
            chosen_name = input("What is your name? ")
            if len(chosen_name) < 1:
                print("Please enter a name that is at least one (1) character long.")
            else:
                self.player_name = chosen_name
                break
    def make_choice(self):
        while True:
            chooses = input("Choose Rock, Paper, or Scissors: ").lower()
            if chooses not in possible_choices:
                print("That is not a valid choice. Please choose again.")
            else:
                self.player_choice = chooses
                break
    def make_winner(self):
        self.is_winner = True