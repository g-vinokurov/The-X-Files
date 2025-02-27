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
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft)
        font = QFont(str(FONT_JET_BRAINS_MONO_NL_BOLD), 11)
        font.setWeight(QFont.Bold)
        self.setFont(font)
    
    def updateUI(self, *args, **kwargs):
        report = self.__report
        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.id}'
        self.setText(text)