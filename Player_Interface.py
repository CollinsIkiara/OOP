# Player Interface

# This code defines a Player interface using an abstract base class (ABC) in Python. The Player class has a method for making moves and an abstract method for leveling up. The Pawn class is a concrete implementation of the Player interface, which defines specific moves and how to level up.

import abc
import random

class Player(abc.ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self): 
        move = random.choice(self.moves)
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position

    @abc.abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),   # up
            (0, -1),  # down
            (-1, 0),  # left
            (1, 0),   # right
        ]

    def level_up(self):
        self.moves += [
            (1, 1),   # up-right
            (-1, 1),  # up-left
            (1, -1),  # down-right
            (-1, -1), # down-left
        ]