
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtCore import Qt

from Gui.Colors import COLOR_VSC_PRIMARY
from Gui.Colors import COLOR_VSC_SECONDARY
from Gui.Colors import COLOR_VSC_TERTIARY


class Scroll(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QScrollArea {{
                background-color: {COLOR_VSC_PRIMARY};
                border-color: {COLOR_VSC_PRIMARY};
            }}

            QScrollBar:horizontal {{
                height: 15px;
                margin: 3px 15px 3px 15px;
                border: 1px transparent {COLOR_VSC_SECONDARY};
                border-radius: 4px;
                background-color: {COLOR_VSC_SECONDARY};
            }}

            QScrollBar::handle:horizontal {{
                background-color: {COLOR_VSC_TERTIARY};
                min-width: 5px;
                border-radius: 4px;
            }}

            QScrollBar::add-line:horizontal {{
                background: none;
            }}

            QScrollBar::sub-line:horizontal {{
                background: none;
            }}

            QScrollBar::up-arrow:horizontal {{
                background: none;
            }}

            QScrollBar::down-arrow:horizontal {{
                background: none;
            }}

            QScrollBar::add-page:horizontal {{
                background: none;
            }}

            QScrollBar::sub-page:horizontal {{
                background: none;
            }}

            QScrollBar:vertical {{
                background-color: {COLOR_VSC_SECONDARY};
                width: 15px;
                margin: 15px 3px 15px 3px;
                border: 1px transparent {COLOR_VSC_SECONDARY};
                border-radius: 4px;
            }}

            QScrollBar::handle:vertical {{
                background-color: {COLOR_VSC_TERTIARY};
                min-height: 5px;
                border-radius: 4px;
            }}

            QScrollBar::add-line:vertical {{
                background: none;
            }}

            QScrollBar::sub-line:vertical {{
                background: none;
            }}

            QScrollBar::up-arrow:vertical {{
                background: none;
            }}

            QScrollBar::down-arrow:vertical {{
                background: none;
            }}

            QScrollBar::add-page:vertical {{
                background: none;
            }}

            QScrollBar::sub-page:vertical {{
                background: none;
            }}
        ''')
