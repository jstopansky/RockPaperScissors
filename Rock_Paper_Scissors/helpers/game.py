from .player import Player

class Game:
    def __init__(self):
        self.userPlayer = Player()
        self.computerPlayer = Player()
        self.winner = None
    def play(self):
        self.userPlayer.getName()
        self.userPlayer.makeChoice()
        
        print(f"You chose {self.userPlayer.playerChoice}")
        print(f"Your opponent chose {self.computerPlayer.playerChoice}")

        if self.userPlayer.playerChoice == self.computerPlayer.playerChoice:
            self.winner = "Tie"
            print("It's a tie!")
        elif self.userPlayer.playerChoice == "rock":
            if self.computerPlayer.playerChoice == "scissors":
                self.winner = self.userPlayer.playerName
                print("Rock crushes scissors. You win!")
            else:
                self.winner = self.computerPlayer.playerName
                print("Paper covers rock. You lose.")
        elif self.userPlayer.playerChoice == "paper":
            if self.computerPlayer.playerChoice == "scissors":
                self.winner = self.computerPlayer.playerName
                print("Scissors cuts paper. You lose.")
            else:
                self.winner = self.userPlayer.playerName
                print("Paper covers rock. You win!")
        elif self.userPlayer.playerChoice == "scissors":
            if self.computerPlayer.playerChoice == "rock":
                self.winner = self.computerPlayer.playerName
                print("Rock crushes scissors. You lose.")
            else:
                self.winner = self.userPlayer.playerName
                print("Scissors cuts paper. You win!")