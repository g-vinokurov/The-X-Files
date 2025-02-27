
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportsList(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._reports = []

        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list {{
                background: transparent;
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)
    
    @property
    def reports(self):
        return self._reports[::]
    
    @reports.setter
    def reports(self, reports: list[Report]):
        pass
