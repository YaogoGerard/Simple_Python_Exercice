#  https://github.com/YaogoGerard
import random


# here ,i create a class player for all player
class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game) -> int:
        raise NotImplementedError


# these are the heritance of class player
class RandomComputerPlayer(Player):
    def _init__(self, letter):
        super().__init__(letter)
    #make a randome choice in available_move()
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def _init__(self, letter):
        super().__init__(letter)

    # in the freecodecamp video, we have the of default return(int) of this fonction comparate to the defauft return(None) of her base
    # got user entry to make move
    def get_move(self, game) -> int:
        while True:
            square = input(self.letter + "'s turn. Input move (0-8):")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                return val
            except ValueError:
                print("Invalid square. Try again.")
