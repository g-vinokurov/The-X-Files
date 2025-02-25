
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font

from Gui.Themes import WELCOME_OPEN_PROJECT_COLOR
from Gui.Themes import WELCOME_OPEN_PROJECT_FONT
from Gui.Themes import WELCOME_OPEN_PROJECT_FONT_WEIGHT
from Gui.Themes import WELCOME_OPEN_PROJECT_FONT_SIZE


class OpenProject(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(f'''
            background: none;
            border: none;
            outline: none;
            padding-top: 16px;
            color: {WELCOME_OPEN_PROJECT_COLOR};
        ''')

        font = Font(WELCOME_OPEN_PROJECT_FONT)
        font.setPointSize(WELCOME_OPEN_PROJECT_FONT_SIZE)
        font.setWeight(WELCOME_OPEN_PROJECT_FONT_WEIGHT)

        self.setFont(font)
