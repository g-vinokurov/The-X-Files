
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from Gui.Widgets.Screens.Screen import Screen

from Gui.Colors import COLOR_WHITE, COLOR_BLACK
from Gui.Fonts import FONT

from Logger import log

from App import app


class Welcome(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding-left: 32px;
            padding-right: 32px;
            padding-top: 32px;
            padding-bottom: 32px;
            color: {COLOR_WHITE};
        ''')
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT), 25))
    
    def updateUI(self, *args, **kwargs):
        self.setText('Welcome!')


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        pass


class Body(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.logo = Welcome(self)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self.logo)
        
        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        self.logo.updateUI(*args, **kwargs)


class Footer(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        pass


class ScreenWelcome(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''background-color: {COLOR_BLACK};''')

        self.header = Header(self)
        self.body = Body(self)
        self.footer = Footer(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self.header)
        self._layout.addWidget(self.body)
        self._layout.addWidget(self.footer)

        self._layout.setStretch(1, 1)
        
        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        self.header.updateUI(*args, **kwargs)
        self.body.updateUI(*args, **kwargs)
        self.footer.updateUI(*args, **kwargs)
        
        app.gui.setWindowTitle('Welcome')
