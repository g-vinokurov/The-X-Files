
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReportsList import ReportsList
from Gui.Widgets.Scrolls import Scroll

from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportsList(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.ArrowCursor))

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(16)
        self._layout.setAlignment(Qt.AlignTop)

        self.setLayout(self._layout)

    def updateUI(self, reports: list[Report] = [], **kwargs):
        for i in reversed(range(self._layout.count())):
            widget = self._layout.itemAt(i).widget()
            if widget is None:
                continue
            widget.setParent(None)
        for report in reversed(sorted(reports, key=lambda r: r.alt_name)):
            report_card = ReportCard(report, self)
            report_card.updateUI()
            self._layout.addWidget(report_card)
    
    @property
    def reports(self):
        return self._reports[::]
    
    @reports.setter
    def reports(self, reports: list[Report]):
        pass
