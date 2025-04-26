
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.NoReportsFoundWidget import NoReportsFoundWidget
from Gui.Widgets.Dashboard.ReportsListContainer import ReportsListContainer
from Gui.Widgets.Dashboard.ReportsListTools import ReportsListTools
from Gui.Widgets.Scrolls import Scroll

import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportsListSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._reports_per_page = 25
        self._pages = 1
        self._page = 1
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-section')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self._tools = ReportsListTools(self)
        self._tools.search_query_field.returnPressed.connect(self._on_search)
        self._tools.search.clicked.connect(self._on_search)
        self._tools.curr_page.returnPressed.connect(self._on_curr_page_changed)
        self._tools.prev_page.clicked.connect(self._on_prev_page_clicked)
        self._tools.next_page.clicked.connect(self._on_next_page_clicked)

        self._no_reports_found = NoReportsFoundWidget(self)
        self._reports_list_container = ReportsListContainer(self)
        self._reports_list_container.hide()

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        self._layout.addWidget(self._tools)
        self._layout.addWidget(self._no_reports_found, stretch=1)
        self._layout.addWidget(self._reports_list_container, stretch=1)

        self.setLayout(self._layout)
        
        self.reports = app.state.project.reports
        self.page = 0
        
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-section {{
                background-color: {Themes.CurrentTheme.DashboardReportsListSectionBackgroundColor};
                outline: none;
                border: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._tools.restyleUI(recursive)
        self._no_reports_found.restyleUI(recursive)
        self._reports_list_container.restyleUI(recursive)
    
    @property
    def reports(self):
        return self._reports_list_container.reports
    
    @reports.setter
    def reports(self, reports: list[Report]):
        if not reports:
            self._reports_list_container.hide()
            self._no_reports_found.show()
        else:
            self._reports_list_container.show()
            self._no_reports_found.hide()

        self._reports_list_container.reports = reports

        if len(reports) != 0:
            self._pages = (len(reports) - 1) // self._reports_per_page + 1
        else:
            self._pages = 0
        self._tools.total_pages.pages = self._pages
    
    @property
    def page(self):
        return self._page
    
    @page.setter
    def page(self, page: int):
        if page < 0 or page > self._pages:
            return
        if page == 0 and self._pages:
            page = 1
        self._page = page
        self._tools.curr_page.setText(str(self._page))
    
    @property
    def pages(self):
        return self._pages
    
    @property
    def reports_list(self):
        return self._reports_list_container.reports_list
    
    def _on_search(self):
        query = self._tools.search_query_field.text()
        log.debug(f'Search: {query}')
        result = app.state.project.search(query)
        self.reports = result
    
    def _on_curr_page_changed(self):
        log.debug(f'Set Current Page: {self._tools.curr_page.text()}')
    
    def _on_prev_page_clicked(self):
        log.debug(f'Previous Page')

    def _on_next_page_clicked(self):
        log.debug(f'Next Page')
