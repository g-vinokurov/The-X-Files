
import enum


class Type(enum.Enum):
    Jeopardy = 0
    Quest = 1
    Machine = 2

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
