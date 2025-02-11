
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter

from PyQt5.QtCore import Qt

from Gui.Widgets.Screens.Screen import Screen
from Gui.Widgets.Scroll import Scroll

from Gui.Colors import COLOR_VSC_PRIMARY
from Gui.Colors import COLOR_VSC_SECONDARY
from Gui.Colors import COLOR_VSC_TERTIARY
from Gui.Colors import COLOR_BS_LIGHT
from Gui.Colors import COLOR_BS_DARK

from Gui.Fonts import FONT_GEOLOGICA_BLACK
from Gui.Fonts import FONT_GEOLOGICA_EXTRA_LIGHT

from Gui.Images import IMG_WELCOME

from State.Models.Project import Project
from State.Models.Report.Report import Report

from Logger import log

from App import app


class ReportTitle(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft)
        self.setFont(QFont(str(FONT_GEOLOGICA_BLACK), 11))
    
    def updateUI(self, report: Report, *args, **kwargs):
        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.alt_name}'
        self.setText(text)


class ReportParameterEmoji(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            font-size: 10pt;
        ''')
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    
    def updateUI(self, emoji: str, *args, **kwargs):
        self.setText(emoji)


class ReportParameter(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_GEOLOGICA_BLACK), 10))
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)


class ReportParameterValue(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_GEOLOGICA_EXTRA_LIGHT), 10))
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)


class ReportParameterItem(QWidget):
    def __init__(self, emoji: str, name: str, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__emoji = emoji
        self.__name = name
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self._emoji = ReportParameterEmoji(self.__emoji, self)
        self._parameter = ReportParameter(self.__name, self)
        self._value = ReportParameterValue(self)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(8)
        self._layout.setAlignment(Qt.AlignTop)
        self._layout.addWidget(self._emoji)
        self._layout.addWidget(self._parameter)
        self._layout.addWidget(self._value)
        self._layout.setStretch(2, 1)

        self.setLayout(self._layout)
    
    def updateUI(self, value: str, *args, **kwargs):
        self._value.setText(value)


class ReportCard(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            border-radius: 16px;
            background-color: {COLOR_BS_LIGHT};
            border-color: none;
            padding: 0px
        ''')

        self._report_title = ReportTitle(self)

        self._report_type = ReportParameterItem('🚩', 'Тип:', self)
        self._report_level = ReportParameterItem('💎', 'Сложность:', self)
        self._report_tags = ReportParameterItem('📌', 'Теги:', self)
        self._report_date = ReportParameterItem('📅', 'Дата:', self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._report_title)
        self._layout.addWidget(self._report_type)
        self._layout.addWidget(self._report_level)
        self._layout.addWidget(self._report_tags)
        self._layout.addWidget(self._report_date)

        self.setLayout(self._layout)

    def updateUI(self, report: Report, *args, **kwargs):
        self._report_title.updateUI(report=report)
        self._report_type.updateUI(value=str(report.type))
        self._report_level.updateUI(value=str(report.level))
        self._report_tags.updateUI(value=', '.join([str(tag) for tag in report.tags]))
        self._report_date.updateUI(value=str(report.date))


class ReportsList(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setStyleSheet(f'''
        #     background-color: {COLOR_VSC_PRIMARY};
        #     border: none;
        # ''')

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
        for report in reports:
            report_card = ReportCard(self)
            report_card.hide()
            report_card.updateUI(report=report)
            self._layout.addWidget(report_card)
            report_card.show()


class ReportsListSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setStyleSheet(f'''
        #     background-color: {COLOR_VSC_PRIMARY};
        #     border: none;
        # ''')

        self._reports_list = ReportsList(self)

        self._scroll = Scroll(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._reports_list)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        project : Project | None = app.state.project
        if project is None:
            log.error(f'Project is not defined')
            return
        self._reports_list.updateUI(reports=project.reports)


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setStyleSheet(f'''background-color: {COLOR_VSC_PRIMARY}''')

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(32, 32, 32, 32)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        pass


class Body(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setStyleSheet(f'''background-color: {COLOR_VSC_PRIMARY}''')

        self._reports_list_section = ReportsListSection(self)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._reports_list_section, stretch=34)
        self._layout.addStretch(55)
        
        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        self._reports_list_section.updateUI(*args, **kwargs)


class Footer(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setStyleSheet(f'''background-color: {COLOR_VSC_PRIMARY}''')
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(32, 32, 32, 32)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        pass


class ScreenDashboard(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        # self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setStyleSheet(f'''background-color: {COLOR_VSC_PRIMARY}''')
        self._background = QPixmap(IMG_WELCOME)

        self._header = Header(self)
        self._body = Body(self)
        self._footer = Footer(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._header)
        self._layout.addWidget(self._body)
        self._layout.addWidget(self._footer)

        self._layout.setStretch(1, 1)
        
        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        self._header.updateUI(*args, **kwargs)
        self._body.updateUI(*args, **kwargs)
        self._footer.updateUI(*args, **kwargs)
        app.gui.setWindowTitle('The X-Files | Dashboard')
    
    def paintEvent(self, event):
        screen_size = self.size()
        screen_width = screen_size.width()
        screen_height = screen_size.height()
        screen_ratio = screen_width / screen_height

        image_width = self._background.width()
        image_height = self._background.height()
        image_ratio = image_width / image_height

        painter = QPainter(self)

        if image_ratio > screen_ratio:
            w = int(screen_height * image_ratio)
            h = screen_height
            x = (w - screen_width) // -2
            y = 0
        else:
            w = screen_width
            h = int(screen_width / image_ratio)
            x = 0
            y = (h - screen_height) // -2
        painter.drawPixmap(x, y, w, h, self._background)