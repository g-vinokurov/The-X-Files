
from PyQt6.QtGui import QPalette


from Ui.Widgets.Screen import Screen


class Welcome(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        pass
