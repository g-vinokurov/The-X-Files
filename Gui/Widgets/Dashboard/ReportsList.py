
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReportCard import ReportCard
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
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list {{
                background-color: transparent;
                outline: none;
                border: none;
                padding: 0px;
            }}
        ''')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(self._layout)

    @property
    def reports(self):
        return self._reports[::]
    
    @reports.setter
    def reports(self, reports: list[Report]):
        for i in range(self._layout.count()):
            widget = self._layout.itemAt(i).widget()
            if widget is None:
                continue
            widget.setParent(None)
        for report in sorted(reports, key=lambda r: r.id, reverse=True):
            report_card = ReportCard(self)
            report_card.report = report
            self._layout.addWidget(report_card)
