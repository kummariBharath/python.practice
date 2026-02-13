from abc import ABC,abstractmethod
from shutil import move
class Player(ABC):
    def __init__(self):
        self.moves=[]
        self.position=(0,0)
        self.path=[self.position]    
    def make_move(self):
        random.choice(moves) 
        new_position=(self.position[0]+move[0],self.position[1]+move[1])
        self.path.append(new_position)
        self.position=new_position
        return self.position
    @abstractmethod
    def level_up(self):