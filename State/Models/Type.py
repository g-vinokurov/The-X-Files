
import enum


class Type(str, enum.Enum):
    
    Jeopardy = 'Jeopardy'  # Standard CTF task in Jeopardy format
    Lab = 'Lab'            # Task where you have to do sth step by step
    Pentest = 'Pentest'    # Pentest

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
