
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class Scroll(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.setStyleSheet(f'''
            QScrollArea {{ 
                background: transparent;
                border: none;
            }}
            
            QScrollArea > QWidget > QWidget {{
                background: transparent; 
                border: none;
            }}

            QScrollBar:horizontal {{
                height: 16px;
                margin: 4px 16px 4px 16px;
                border: 1px transparent {Theme.ScrollHorizontalBorderColor};
                border-radius: {Theme.ScrollHorizontalBorderRadius}px;
                background-color: transparent;
            }}

            QScrollBar::handle:horizontal {{
                background-color: {Theme.ScrollHorizontalHandleBackgroundColor};
                min-width: 8px;
                border-radius: {Theme.ScrollHorizontalHandleBorderRadius}px;
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
                background-color: transparent;
                width: 16px;
                margin: 16px 4px 16px 4px;
                border: 1px transparent {Theme.ScrollVerticalBorderColor};
                border-radius: {Theme.ScrollVerticalBorderRadius}px;
            }}

            QScrollBar::handle:vertical {{
                background-color: {Theme.ScrollVerticalHandleBackgroundColor};
                min-height: 8px;
                border-radius: {Theme.ScrollVerticalHandleBorderRadius}px;
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


class ScrollPre(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.setStyleSheet(f'''
            QScrollArea {{ 
                background: transparent;
                border: none;
            }}
            
            QScrollArea > QWidget > QWidget {{
                background: transparent; 
                border: none;
            }}

            QScrollBar:horizontal {{
                height: 16px;
                margin: 4px 16px 4px 16px;
                border: 1px transparent {Theme.ScrollPreHorizontalBorderColor};
                border-radius: {Theme.ScrollPreHorizontalBorderRadius}px;
                background-color: transparent;
            }}

            QScrollBar::handle:horizontal {{
                background-color: {Theme.ScrollPreHorizontalHandleBackgroundColor};
                min-width: 8px;
                border-radius: {Theme.ScrollPreHorizontalHandleBorderRadius}px;
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
                background-color: transparent;
                width: 16px;
                margin: 16px 4px 16px 4px;
                border: 1px transparent {Theme.ScrollPreVerticalBorderColor};
                border-radius: {Theme.ScrollPreVerticalBorderRadius}px;
            }}

            QScrollBar::handle:vertical {{
                background-color: {Theme.ScrollPreVerticalHandleBackgroundColor};
                min-height: 8px;
                border-radius: {Theme.ScrollPreVerticalHandleBorderRadius}px;
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
