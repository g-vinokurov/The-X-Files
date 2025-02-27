
class ReportParameterEmoji(QLabel):
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