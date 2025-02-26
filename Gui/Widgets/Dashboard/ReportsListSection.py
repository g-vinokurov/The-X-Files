
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class ReportsListSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-section')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-section {{
                background-color: {Theme.DashboardReportsListSectionBackgroundColor};
                outline: none;
                border: none;
                padding: 0px;
            }}
        ''')

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(32, 32, 32, 32)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self._layout)
