class ReportFileWidget(QWidget):
    def __init__(self, dir: str, file: File, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__dir = dir
        self.__file = file
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            background: none;
            border: none;
        ''')

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 8)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignLeft)

        self._report_file_emoji = ReportParameterEmoji('📌', self)
        self._report_file = ReportParameter(f'{self.__file.name}:', self)
        self._report_file_value = ReportLinkValue(f'{self.__file.src}', self)

        self._layout.addWidget(self._report_file_emoji)
        self._layout.addWidget(self._report_file)
        self._layout.addWidget(self._report_file_value)

        self._layout.setStretch(2, 1)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._report_file_value.updateUI(self.__file.src)