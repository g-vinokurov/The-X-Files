
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

from Config import FONTS_DIR

from Logger import log


class Font:
    def __init__(self, filepath: str):
        self.__filepath = filepath
        self.__family = None

    def __str__(self):
        if self.__family is not None:
            return str(self.__family)
        
        if QApplication.instance() is None:
            log.warning('QApplication not started - impossible to load font')
            return str()
        
        font_id = QFontDatabase.addApplicationFont(self.__filepath)
        if font_id == -1:
            log.warning(f'Could not load font {self.__filepath}')
            return str()

        families = QFontDatabase.applicationFontFamilies(font_id)
        if not families:
            return str()

        self.__family = families[0]
        return str(self.__family)


FONT_GEOLOGICA_BLACK = Font(os.path.join(FONTS_DIR, 'Geologica-Black.ttf'))
FONT_GEOLOGICA_BOLD = Font(os.path.join(FONTS_DIR, 'Geologica-Bold.ttf'))
FONT_GEOLOGICA_EXTRA_BOLD = Font(os.path.join(FONTS_DIR, 'Geologica-ExtraBold.ttf'))
FONT_GEOLOGICA_EXTRA_LIGHT = Font(os.path.join(FONTS_DIR, 'Geologica-ExtraLight.ttf'))
FONT_GEOLOGICA_LIGHT = Font(os.path.join(FONTS_DIR, 'Geologica-Light.ttf'))
FONT_GEOLOGICA_MEDIUM = Font(os.path.join(FONTS_DIR, 'Geologica-Medium.ttf'))
FONT_GEOLOGICA_REGULAR = Font(os.path.join(FONTS_DIR, 'Geologica-Regular.ttf'))
FONT_GEOLOGICA_SEMI_BOLD = Font(os.path.join(FONTS_DIR, 'Geologica-SemiBold.ttf'))
FONT_GEOLOGICA_THIN = Font(os.path.join(FONTS_DIR, 'Geologica-Thin.ttf'))
