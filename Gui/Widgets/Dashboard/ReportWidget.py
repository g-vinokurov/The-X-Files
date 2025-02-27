
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportWidget(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._report = None

        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-report-widget {{
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
    def report(self):
        return self._report
    
    @report.setter
    def report(self, report: Report | None):
        if report == self._report:
            return
        if report is None:
            return
        log.info(f'Report {report.id} selected')
