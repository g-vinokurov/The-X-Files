class ReportParagraph(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding: 0px;
            color: {COLOR_BS_DARK};
        ''')
        self.setContentsMargins(0, 0, 0, 8)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 10))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        pass