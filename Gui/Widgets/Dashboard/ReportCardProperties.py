
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReportPropertyEmoji import ReportPropertyEmoji
from Gui.Widgets.Dashboard.ReportPropertyName import ReportPropertyName
from Gui.Widgets.Dashboard.ReportPropertyValue import ReportPropertyValue

from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportCardProperties(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._report = None
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-card-properties')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-report-card-properties {{
                background-color: transparent;
                border: none;
                padding: 0px;
                outline: none;
            }}
        ''')

        self._layout = QGridLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._report_type_emoji = ReportPropertyEmoji('🚩', self)
        self._report_type = ReportPropertyName('Type:', self)
        self._report_type_value = ReportPropertyValue(self)

        self._report_level_emoji = ReportPropertyEmoji('☢️', self)
        self._report_level = ReportPropertyName('Level:', self)
        self._report_level_value = ReportPropertyValue(self)

        self._report_tags_emoji = ReportPropertyEmoji('🌵', self)
        self._report_tags = ReportPropertyName('Tags:', self)
        self._report_tags_value = ReportPropertyValue(self)

        self._report_date_emoji = ReportPropertyEmoji('☄️', self)
        self._report_date = ReportPropertyName('Date:', self)
        self._report_date_value = ReportPropertyValue(self)

        self._layout.addWidget(self._report_type_emoji, 0, 0)
        self._layout.addWidget(self._report_type, 0, 1)
        self._layout.addWidget(self._report_type_value, 0, 2)

        self._layout.addWidget(self._report_level_emoji, 1, 0)
        self._layout.addWidget(self._report_level, 1, 1)
        self._layout.addWidget(self._report_level_value, 1, 2)

        self._layout.addWidget(self._report_tags_emoji, 2, 0)
        self._layout.addWidget(self._report_tags, 2, 1)
        self._layout.addWidget(self._report_tags_value, 2, 2)

        self._layout.addWidget(self._report_date_emoji, 3, 0)
        self._layout.addWidget(self._report_date, 3, 1)
        self._layout.addWidget(self._report_date_value, 3, 2)

        self._layout.setColumnStretch(2, 1)

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
        self._report = report

        report_type = '-' if self._report.type is None else self._report.type
        report_level = '-' if self._report.level is None else self._report.level
        report_tags = ', '.join(map(str, self._report.tags))
        report_tags = report_tags if report_tags else 'No tags'
        report_date = '-' if self._report.date is None else self._report.date

        self._report_type_value.value = str(report_type)
        self._report_level_value.value = str(report_level)
        self._report_tags_value.value = str(report_tags)
        self._report_date_value.value = str(report_date)
