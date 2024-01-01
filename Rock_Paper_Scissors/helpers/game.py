from .player import Player

class Game:
    def __init__(self):
        self.user_player = Player()
        self.computer_player = Player()
        self.winner = None
    def play(self):
        self.user_player.get_name()
        self.user_player.make_choice()
        
        print(f"You chose {self.user_player.player_choice}")
        print(f"Your opponent chose {self.computer_player.player_choice}")

        if self.user_player.player_choice == self.computer_player.player_choice:
            self.winner = "Tie"
            print("It's a tie!")
        elif self.user_player.player_choice == "rock":
            if self.computer_player.player_choice == "scissors":
                self.winner = self.user_player.player_name
                print("Rock crushes scissors. You win!")
            else:
                self.winner = self.computer_player.player_name
                print("Paper covers rock. You lose.")
        elif self.user_player.player_choice == "paper":
            if self.computer_player.player_choice == "scissors":
                self.winner = self.computer_player.player_name
                print("Scissors cuts paper. You lose.")
            else:
                self.winner = self.user_player.player_name
                print("Paper covers rock. You win!")
        elif self.user_player.player_choice == "scissors":
            if self.computer_player.player_choice == "rock":
                self.winner = self.computer_player.player_name
                print("Rock crushes scissors. You lose.")
            else:
                self.winner = self.user_player.player_name
                print("Scissors cuts paper. You win!")