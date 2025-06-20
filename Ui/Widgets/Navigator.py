
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QGridLayout

from Ui.Widgets.Screen import Screen


class Navigator(QWidget):
    _mapper : dict[str, Screen] = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._screens : dict[str, Screen] = {}
        self.initUI()

    def initUI(self):
        self._current_screen = Screen(self)

        self._layout = QGridLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self._current_screen)

        self.setLayout(self._layout)

    def load(self, tag: str, *args, **kwargs):
        self._screens[tag] = self._mapper.get(tag, Screen)(self, *args, **kwargs)
        self._screens[tag].hide()

    def goto(self, tag: str, *args, **kwargs):
        if tag not in self._screens:
            self.load(tag, *args, **kwargs)

        self._layout.removeWidget(self._current_screen)
        self._current_screen.hide()
        self._current_screen : Screen = self._screens[tag]
        self._current_screen.show()
        self._layout.addWidget(self._current_screen)

    @classmethod
    def add(cls, tag: str, screen_cls: type[Screen]):
        if tag in cls._mapper:
            return
        cls._mapper[tag] = screen_cls
    
    @property
    def screen(self):
        return self._current_screen
