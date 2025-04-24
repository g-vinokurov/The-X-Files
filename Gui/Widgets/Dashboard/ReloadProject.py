
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

# from State.Utils.ProjectLoader import ProjectLoader
# from State.Utils.Desktop import Desktop

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log


class ReloadProject(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reload-project')

        self.setStyleSheet(f'''
            QPushButton#dashboard-reload-project {{
                color: {Theme.DashboardReloadProjectColor};
                background: {Theme.DashboardReloadProjectBackgroundColor};
                border: 1px solid {Theme.DashboardReloadProjectBorderColor};
                outline: none;
                padding-left: 32px;
                padding-top: 4px;
                padding-right: 32px;
                padding-bottom: 4px;
            }}

            QPushButton#dashboard-reload-project:hover {{
                color: {Theme.DashboardReloadProjectHoverColor};
                background: {Theme.DashboardReloadProjectHoverBackgroundColor};
            }}
        ''')
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Theme.DashboardReloadProjectFont)
        font.setPointSize(Theme.DashboardReloadProjectFontSize)
        font.setWeight(Theme.DashboardReloadProjectFontWeight)
        self.setFont(font)
