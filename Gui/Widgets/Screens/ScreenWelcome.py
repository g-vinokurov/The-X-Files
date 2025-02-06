
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter

from PyQt5.QtCore import Qt

from Gui.Widgets.Screens.Screen import Screen

from Gui.Colors import COLOR_WHITE
from Gui.Colors import COLOR_BLACK
from Gui.Colors import COLOR_VSC_PRIMARY
from Gui.Colors import COLOR_BS_LIGHT

from Gui.Fonts import FONT_GEOLOGICA_BLACK
from Gui.Fonts import FONT_COURIER_PRIME

from Gui.Images import IMG_WELCOME

from Logger import log

from App import app


class Logo(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding-left: 0px;
            padding-right: 0px;
            padding-top: 0px;
            padding-bottom: 0px;
            color: {COLOR_BS_LIGHT};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_COURIER_PRIME), 48))
    
    def updateUI(self, *args, **kwargs):
        self.setText('THE X-FILES')


class ClickToContinue(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            background: none;
            border: none;
            outline: none;
            color: {COLOR_BS_LIGHT};
        ''')
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_COURIER_PRIME), 18))
    
    def updateUI(self):
        self.setText('Click to continue')


class ScreenWelcome(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.background = QPixmap(IMG_WELCOME)
        self.logo = Logo(self)
        self.click_to_continue = ClickToContinue(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self.logo)
        self._layout.addWidget(self.click_to_continue)
        
        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        app.gui.setWindowTitle('The X-Files')
        self.logo.updateUI(*args, **kwargs)
        self.click_to_continue.updateUI(*args, **kwargs)
    
    def paintEvent(self, event):
        screen_size = self.size()
        screen_width = screen_size.width()
        screen_height = screen_size.height()
        screen_ratio = screen_width / screen_height

        image_width = self.background.width()
        image_height = self.background.height()
        image_ratio = image_width / image_height

        painter = QPainter(self)

        if image_ratio > screen_ratio:
            w = int(screen_height * image_ratio)
            h = screen_height
            x = (w - screen_width) // -2
            y = 0
        else:
            w = screen_width
            h = int(screen_width / image_ratio)
            x = 0
            y = (h - screen_height) // -2
        painter.drawPixmap(x, y, w, h, self.background)
    
    def mousePressEvent(self, event):
        log.info('Go to dashboard')
