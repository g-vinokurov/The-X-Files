class ReportImageWidget(QWidget):
    def __init__(self, report_dir: str, img: Img, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dir = report_dir
        self.__src = img.src
        self.__text = img.name
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        path = pathlib.Path(self.__dir) / pathlib.Path(self.__src)

        self._image = ReportImageContent(path, self)
        self._image_title = ReportImageTitle(self.__text, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self._image)
        self._layout.addWidget(self._image_title)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._image.updateUI(*args, **kwargs)
        self._image_title.updateUI(*args, **kwargs)



class ReportImageContent(QWidget):
    def __init__(self, path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__path = path
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._pixmap = QPixmap.fromImage(QImage(str(self.__path)))
        
        # This code allows show image via QLabel in layout
        # If image is too large it will fit to layout size
        # Usage: if we need scale image to full layout width
        self._image = QLabel("", self)
        self._image.setMinimumSize(1, 1)
        self._image.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._image.setAlignment(Qt.AlignCenter)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(8, 8, 8, 8)
        self._layout.setSpacing(4)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self._image)

        self.setLayout(self._layout)
    
    def updateUI(self, *args, **kwargs):
        self._image.setPixmap(self._pixmap)
        pass

    def resizeEvent(self, event):
        pixmap = self._pixmap.scaledToWidth(self._image.width(), Qt.TransformationMode.SmoothTransformation)
        self._image.setPixmap(pixmap)


class ReportImageTitle(QLabel):
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
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_REGULAR), 10))
        self.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.IBeamCursor))
    
    def updateUI(self, *args, **kwargs):
        pass