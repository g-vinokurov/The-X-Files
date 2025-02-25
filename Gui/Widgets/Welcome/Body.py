
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Welcome.Logo import Logo
from Gui.Widgets.Welcome.OpenProject import OpenProject


class Body(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._logo = Logo('THE X-FILES', self)
        self._open_project = OpenProject('Open Project', self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self._logo)
        self._layout.addWidget(self._open_project)

        self.setLayout(self._layout)
