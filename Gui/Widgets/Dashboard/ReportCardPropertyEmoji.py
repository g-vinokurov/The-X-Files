
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportCardPropertyEmoji(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-card-property-emoji')
        self.setStyleSheet(f'''
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        font = Font(Themes.CurrentTheme.DashboardReportCardPropertyEmojiFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportCardPropertyEmojiFontSize)
        font.setHintingPreference(Font.HintingPreference.PreferNoHinting)
        self.setFont(font)

        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        pass
