
import pathlib

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

from Config import FONTS_DIR

from Logger import log


class Font:
    def __init__(self, filepath: str | pathlib.Path):
        self.__filepath = str(filepath)
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


FONT_SEGOE_UI_EMOJI = Font(FONTS_DIR / 'Segoe-UI-Emoji.ttf')

FONT_GEOLOGICA_BLACK = Font(FONTS_DIR / 'Geologica-Black.ttf')
FONT_GEOLOGICA_BOLD = Font(FONTS_DIR / 'Geologica-Bold.ttf')
FONT_GEOLOGICA_EXTRA_BOLD = Font(FONTS_DIR / 'Geologica-ExtraBold.ttf')
FONT_GEOLOGICA_EXTRA_LIGHT = Font(FONTS_DIR / 'Geologica-ExtraLight.ttf')
FONT_GEOLOGICA_LIGHT = Font(FONTS_DIR / 'Geologica-Light.ttf')
FONT_GEOLOGICA_MEDIUM = Font(FONTS_DIR / 'Geologica-Medium.ttf')
FONT_GEOLOGICA_REGULAR = Font(FONTS_DIR / 'Geologica-Regular.ttf')
FONT_GEOLOGICA_SEMI_BOLD = Font(FONTS_DIR / 'Geologica-SemiBold.ttf')
FONT_GEOLOGICA_THIN = Font(FONTS_DIR / 'Geologica-Thin.ttf')

FONT_JET_BRAINS_MONO_NL_BOLD = Font(FONTS_DIR / 'JetBrainsMonoNL-Bold.ttf')
FONT_JET_BRAINS_MONO_NL_EXTRA_BOLD = Font(FONTS_DIR / 'JetBrainsMonoNL-ExtraBold.ttf')
FONT_JET_BRAINS_MONO_NL_EXTRA_LIGHT = Font(FONTS_DIR / 'JetBrainsMonoNL-ExtraLight.ttf')
FONT_JET_BRAINS_MONO_NL_LIGHT = Font(FONTS_DIR / 'JetBrainsMonoNL-Light.ttf')
FONT_JET_BRAINS_MONO_NL_MEDIUM = Font(FONTS_DIR / 'JetBrainsMonoNL-Medium.ttf')
FONT_JET_BRAINS_MONO_NL_REGULAR = Font(FONTS_DIR / 'JetBrainsMonoNL-Regular.ttf')
FONT_JET_BRAINS_MONO_NL_SEMI_BOLD = Font(FONTS_DIR / 'JetBrainsMonoNL-SemiBold.ttf')
FONT_JET_BRAINS_MONO_NL_THIN = Font(FONTS_DIR / 'JetBrainsMonoNL-Thin.ttf')
