class ReportCardAltName(QLabel):
    def __init__(self, report: Report, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__report = report
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_SECONDARY};
        ''')
        self.setContentsMargins(0, 0, 0, 8)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 9))

        self.setText(str(self.__report.id))
    
    def updateUI(self, *args, **kwargs):
        pass
