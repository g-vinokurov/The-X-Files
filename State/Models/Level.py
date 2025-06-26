
import enum


class Level(str, enum.Enum):
    Baby = 'Baby'
    Easy = 'Easy'
    Middle = 'Middle'
    Hard = 'Hard'
    Insane = 'Insane'

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
