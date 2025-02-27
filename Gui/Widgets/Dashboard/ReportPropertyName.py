
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class ReportPropertyName(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-property-name')
        
        self.setStyleSheet(f'''
            color: {Theme.DashboardReportPropertyNameColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        font = Font(Theme.DashboardReportPropertyNameFont)
        font.setPointSize(Theme.DashboardReportPropertyNameFontSize)
        font.setWeight(Theme.DashboardReportPropertyNameFontWeight)
        self.setFont(font)
