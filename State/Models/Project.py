
class Project:
    def __init__(self, dir: str):
        self._dir = dir
    
    @property
    def dir(self):
        return self._dir
    
    @classmethod
    def open(cls, dir: str):
        return cls(dir)
