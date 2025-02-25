
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font

from Gui.Themes import WELCOME_LOGO_COLOR
from Gui.Themes import WELCOME_LOGO_FONT
from Gui.Themes import WELCOME_LOGO_FONT_WEIGHT
from Gui.Themes import WELCOME_LOGO_FONT_SIZE


class Logo(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {WELCOME_LOGO_COLOR};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)

        font = Font(WELCOME_LOGO_FONT)
        font.setPointSize(WELCOME_LOGO_FONT_SIZE)
        font.setWeight(WELCOME_LOGO_FONT_WEIGHT)

        self.setFont(font)
