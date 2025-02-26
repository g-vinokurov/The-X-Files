
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReportsListSection import ReportsListSection
from Gui.Widgets.Dashboard.ReportSection import ReportSection
from Gui.Widgets.Splitter import Splitter

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class Body(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-body')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-body {{
                background-color: {Theme.DashboardBodyBackgroundColor};
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')

        self._reports_list_section = ReportsListSection(self)
        self._report_section = ReportSection(self)

        self._splitter = Splitter(Qt.Orientation.Horizontal)
        self._splitter.addWidget(self._reports_list_section)
        self._splitter.addWidget(self._report_section)
        self._splitter.setStretchFactor(0, 34)
        self._splitter.setStretchFactor(1, 55)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._splitter)

        self.setLayout(self._layout)
    
    @property
    def reports_list_section(self):
        return self._reports_list_section
    
    @property
    def report_section(self):
        return self._report_section
