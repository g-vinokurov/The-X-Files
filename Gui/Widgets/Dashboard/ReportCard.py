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
        self._report_alt_name = ReportCardAltName(self.__report, self)
        self._report_parameters = ReportCardParameters(self.__report, self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignTop)

        self._layout.addWidget(self._report_title)
        self._layout.addWidget(self._report_alt_name)
        self._layout.addWidget(self._report_parameters)

        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        self._report_title.updateUI(*args, **kwargs)
        self._report_alt_name.updateUI(*args, **kwargs)
        self._report_parameters.updateUI(*args, **kwargs)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            app.gui.navigator.update('dashboard', current_report=self.__report)