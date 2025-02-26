
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
from Gui.Themes import DefaultTheme as Theme

from Log import log
from App import app


class OpenProject(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('welcome-open-project')

        self.setStyleSheet(f'''
            color: {Theme.WelcomeOpenProjectColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Theme.WelcomeOpenProjectFont)
        font.setPointSize(Theme.WelcomeOpenProjectFontSize)
        font.setWeight(Theme.WelcomeOpenProjectFontWeight)
        self.setFont(font)

        self.setText('Open Project')
