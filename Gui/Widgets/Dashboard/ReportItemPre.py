
class ReportPreformatted(QWidget):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text = text
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.IBeamCursor))
        self.setStyleSheet(f'''
            padding: 0px;
            background-color: {COLOR_BS_GRAY_200};
            border-radius: 16px;
            border-color: none;
            color: {COLOR_BS_DARK};
        ''')

        self._widget = ReportPreformattedWidget(self.__text, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)
        
        self._layout.addWidget(self._widget)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._widget.updateUI(*args, **kwargs)


class ReportPreformattedWidget(QWidget):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text = text
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._content = ReportPreformattedWidgetContent(self.__text, self)

        self._scroll = ScrollSecondary(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._content)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._content.updateUI(*args, **kwargs)



class ReportPreformattedWidgetContent(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setContentsMargins(8, 8, 8, 8)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 9))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        pass

