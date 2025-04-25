
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

from Gui.Widgets.Dashboard.ReportCardTitle import ReportCardTitle
from Gui.Widgets.Dashboard.ReportCardId import ReportCardId
from Gui.Widgets.Dashboard.ReportCardProperties import ReportCardProperties

import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportCard(QWidget):
    selected = pyqtSignal(Report)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._report = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-card')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self._report_title = ReportCardTitle(self)
        self._report_id = ReportCardId(self)
        self._report_properties = ReportCardProperties(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(32, 32, 32, 32)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._layout.addWidget(self._report_title)
        self._layout.addWidget(self._report_id)
        self._layout.addWidget(self._report_properties)

        self.setLayout(self._layout)
        self.restyleUI()
    
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
        
        self._report_title.report = report
        self._report_id.report = report
        self._report_properties.report = report
    
    def mouseDoubleClickEvent(self, event):
        if self._report is None:
            return
        self.selected.emit(self._report)
    
    def restyleUI(self):
        self.setStyleSheet(f'''
            QWidget#dashboard-report-card {{
                background-color: {Themes.CurrentTheme.DashboardReportCardBackgroundColor};
                border-bottom: 1px solid {Themes.CurrentTheme.DashboardReportCardBorderColor};
                border-right: 1px solid {Themes.CurrentTheme.DashboardReportCardBorderColor};
                padding: 0px;
                outline: none;
            }}

            QWidget#dashboard-report-card:hover {{
                background-color: {Themes.CurrentTheme.DashboardReportCardHoveredBackgroundColor};
            }}
        ''')
        self._report_title.restyleUI()
        self._report_id.restyleUI()
        self._report_properties.restyleUI()
