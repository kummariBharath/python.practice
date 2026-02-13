import random
from abc import ABC,abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.position=(0,0)
        self.path=[self.position]    
    def make_move(self):
        move = random.choice(self.moves) 
        new_position=(self.position[0]+move[0],self.position[1]+move[1])
        self.path.append(new_position)
        self.position=new_position
        return self.position
    @abstractmethod
    def level_up(self):
        pass