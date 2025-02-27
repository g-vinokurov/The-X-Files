class ReportParameter(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_BOLD), 10))
    
    def updateUI(self, text: str, *args, **kwargs):
        self.setText(text)