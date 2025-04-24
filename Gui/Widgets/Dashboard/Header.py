
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReloadProject import ReloadProject

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-header')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-header {{
                background-color: {Theme.DashboardHeaderBackgroundColor};
                border-bottom: 1px solid {Theme.DashboardHeaderBorderColor};
                outline: none;
                padding: 0px;
            }}
        ''')

        self._reload_project = ReloadProject('Reload Project', self)
        self._reload_project.clicked.connect(self._on_reload_project_clicked)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(32, 16, 32, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self._layout.addWidget(self._reload_project)

        self.setLayout(self._layout)
    
    def _on_reload_project_clicked(self):
        pass
