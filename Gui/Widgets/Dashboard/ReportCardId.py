
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportCardId(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-card-id')

        self.setStyleSheet(f'''
            color: {Theme.DashboardReportCardIdColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setContentsMargins(0, 0, 0, 8)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        font = Font(Theme.DashboardReportCardIdFont)
        font.setPointSize(Theme.DashboardReportCardIdFontSize)
        font.setWeight(Theme.DashboardReportCardIdFontWeight)
        self.setFont(font)
    
    @property
    def report(self):
        return self._report
    
    @report.setter
    def report(self, report: Report | None):
        if report == self._report:
            return
        if report is None:
            return 
        self._report = report
        text = f'{report.id}'
        self.setText(text)
