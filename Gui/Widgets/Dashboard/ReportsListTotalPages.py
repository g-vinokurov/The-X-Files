
from PyQt5.QtWidgets import QLabel

from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportsListTotalPages(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-total-pages')

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setWordWrap(False)
        
        font = Font(Themes.CurrentTheme.DashboardReportsListTotalPagesFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportsListTotalPagesFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportsListTotalPagesFontWeight)
        self.setFont(font)

        self.adjustHeight()
        self.setText('of  1000')
        self.restyleUI()
    
    # If word-wrap is True, QLabel does not resize automatically and hide parts of text
    def adjustHeight(self):
        font_metrics = self.fontMetrics()
        width = self.width()
        text = self.text()
        text_rect = font_metrics.boundingRect(0, 0, width, 0, Qt.TextFlag.TextWordWrap, text)
        required_height = text_rect.height()
        self.setMinimumHeight(required_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustHeight()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportsListTotalPagesColor};
            background: none;
            border: none;
            border-left: 1px solid {Themes.CurrentTheme.DashboardReportsListTotalPagesBorderColor};
            outline: none;
            padding-left: 16px;
            padding-top: 4px;
            padding-right: 16px;
            padding-bottom: 4px;
        ''')
