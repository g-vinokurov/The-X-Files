
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
from Gui.Fonts import FONT_NOTO_EMOJI_SEMI_BOLD
from Gui.Fonts import FONT_SEGOE_UI_EMOJI

from Gui.Images import IMG_WELCOME

from State.Models.Project import Project
from State.Models.Report.Report import Report

from Logger import log

from App import app


class ReportCardTitle(QLabel):
    def __init__(self, report: Report, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__report = report
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft)
        self.setFont(QFont(str(FONT_GEOLOGICA_BLACK), 11))
    
    def updateUI(self, *args, **kwargs):
        report = self.__report
        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.alt_name}'
        self.setText(text)


class ReportWidgetTitle(QLabel):
    def __init__(self, report: Report, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__report = report
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_GEOLOGICA_BLACK), 12))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        report = self.__report
        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.alt_name}'
        self.setText(text)


class ReportCardParameterEmoji(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        font = QFont(str(FONT_SEGOE_UI_EMOJI), 12)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.setFont(font)
    
    def updateUI(self, emoji: str, *args, **kwargs):
        self.setText(emoji)


class ReportCardParameter(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_GEOLOGICA_BLACK), 10))
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)


class ReportCardParameterValue(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_GEOLOGICA_EXTRA_LIGHT), 10))
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)


class ReportCardParameters(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')

        self._layout = QGridLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignTop)

        self._report_type_emoji = ReportCardParameterEmoji('🚩', self)
        self._report_type = ReportCardParameter('Тип:', self)
        self._report_type_value = ReportCardParameterValue(self)

        self._report_level_emoji = ReportCardParameterEmoji('☢️', self)
        self._report_level = ReportCardParameter('Уровень:', self)
        self._report_level_value = ReportCardParameterValue(self)

        self._report_tags_emoji = ReportCardParameterEmoji('🌵', self)
        self._report_tags = ReportCardParameter('Теги:', self)
        self._report_tags_value = ReportCardParameterValue(self)

        self._report_date_emoji = ReportCardParameterEmoji('☄️', self)
        self._report_date = ReportCardParameter('Дата:', self)
        self._report_date_value = ReportCardParameterValue(self)

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
    
    def updateUI(self, *args, **kwargs):
        report = self.__report

        report_type = str(report.type) if report.type is not None else 'Undefined'
        report_level = str(report.level) if report.level is not None else 'Undefined'
        report_tags = [str(tag) for tag in report.tags]
        report_tags = ', '.join(report_tags) if report_tags else 'No tags'
        report_date = str(report.date) if report.date is not None else 'Undefined'

        self._report_type_value.updateUI(report_type)
        self._report_level_value.updateUI(report_level)
        self._report_tags_value.updateUI(report_tags)
        self._report_date_value.updateUI(report_date)


class ReportCard(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            border-radius: 16px;
            background-color: {COLOR_BS_LIGHT};
            border-color: none;
            padding: 0px
        ''')
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self._report_title = ReportCardTitle(self.__report, self)
        self._report_parameters = ReportCardParameters(self.__report, self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._report_title)
        self._layout.addWidget(self._report_parameters)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        self._report_title.updateUI(*args, **kwargs)
        self._report_parameters.updateUI(*args, **kwargs)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            app.gui.navigator.update('dashboard', current_report=self.__report)


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
        for report in reports:
            report_card = ReportCard(report, self)
            report_card.updateUI()
            self._layout.addWidget(report_card)


class ReportsListSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.ArrowCursor))

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


class ReportWidgetContent(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            border-radius: 16px;
            background-color: {COLOR_BS_LIGHT};
            border-color: none;
            padding: 0px
        ''')
        self.setCursor(QCursor(Qt.ArrowCursor))

        self._report_title = ReportWidgetTitle(self.__report, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(32, 32, 32, 32)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._report_title)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._report_title.updateUI(*args, **kwargs)


class ReportWidget(QWidget):
    def __init__(self, report: Report, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.ArrowCursor))

        self._report_content = ReportWidgetContent(self.__report, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._report_content)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._report_content.updateUI(*args, **kwargs)


class ReportSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._report_widget = None

        self._scroll = Scroll(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(None)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)

    def updateUI(self, *args, report: Report | None = None, **kwargs):
        if report is None:
            self._scroll.setWidget(None)
            self._report_widget = None
            return
        self._report_widget = ReportWidget(report, self)
        self._report_widget.updateUI(*args, **kwargs)
        self._scroll.setWidget(self._report_widget)


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

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

        self._reports_list_section = ReportsListSection(self)
        self._report_section = ReportSection(self)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._reports_list_section, stretch=34)
        self._layout.addWidget(self._report_section, stretch=55)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        current_report = kwargs.pop('current_report', None)
        self._reports_list_section.updateUI(*args, **kwargs)
        self._report_section.updateUI(*args, report=current_report, **kwargs)


class Footer(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        pass


class ScreenDashboard(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
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

    def updateUI(self, *args, current_report: Report | None = None, **kwargs):
        kwargs['current_report'] = current_report
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