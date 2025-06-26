
from PyQt6.QtWidgets import QApplication

from Ui.Widgets.Window import Window
from State.State import State


class App(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__([])
        
        self._state : State = State()
        self._gui : Window = Window()
    
    @property
    def state(self):
        return self._state
    
    @property
    def gui(self):
        return self._gui
    
    def start(self, tag: str):
        self._gui.navigator.goto(tag)
        self._gui.show()
        self.exec()

app = App()
