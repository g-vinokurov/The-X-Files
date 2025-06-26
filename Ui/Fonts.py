
import pathlib

from PyQt6.QtWidgets import QApplication

from PyQt6.QtGui import QFontDatabase
from PyQt6.QtGui import QFont

from Config import DIR_FONTS

from Log import log


class FileFont(QFont):    
    _loaded_fonts = {}
    
    def __init__(self, path: str | pathlib.Path):
        path = str(path)
        if path not in self._loaded_fonts:
            self._load(path)
        font = self._loaded_fonts.get(path)
        super().__init__(font)
    
    @classmethod
    def _load(cls, path: str):

        if QApplication.instance() is None:
            log.warning('App not started - could not load fonts')
            return
        
        font_id = QFontDatabase.addApplicationFont(path)
        if font_id == -1:
            log.warning(f'Could not load font {path}')
            return

        families = QFontDatabase.applicationFontFamilies(font_id)
        if not families:
            return

        cls._loaded_fonts[path] = font = families[0]

        log.info(f'Font {font} loaded')


FONT_GEOLOGICA_BLACK       = DIR_FONTS / 'Geologica-Black.ttf'
FONT_GEOLOGICA_BOLD        = DIR_FONTS / 'Geologica-Bold.ttf'
FONT_GEOLOGICA_EXTRA_BOLD  = DIR_FONTS / 'Geologica-ExtraBold.ttf'
FONT_GEOLOGICA_EXTRA_LIGHT = DIR_FONTS / 'Geologica-ExtraLight.ttf'
FONT_GEOLOGICA_LIGHT       = DIR_FONTS / 'Geologica-Light.ttf'
FONT_GEOLOGICA_MEDIUM      = DIR_FONTS / 'Geologica-Medium.ttf'
FONT_GEOLOGICA_REGULAR     = DIR_FONTS / 'Geologica-Regular.ttf'
FONT_GEOLOGICA_SEMI_BOLD   = DIR_FONTS / 'Geologica-SemiBold.ttf'
FONT_GEOLOGICA_THIN        = DIR_FONTS / 'Geologica-Thin.ttf'

FONT_JET_BRAINS_MONO_NL_BOLD        = DIR_FONTS / 'JetBrainsMonoNL-Bold.ttf'
FONT_JET_BRAINS_MONO_NL_EXTRA_BOLD  = DIR_FONTS / 'JetBrainsMonoNL-ExtraBold.ttf'
FONT_JET_BRAINS_MONO_NL_EXTRA_LIGHT = DIR_FONTS / 'JetBrainsMonoNL-ExtraLight.ttf'
FONT_JET_BRAINS_MONO_NL_LIGHT       = DIR_FONTS / 'JetBrainsMonoNL-Light.ttf'
FONT_JET_BRAINS_MONO_NL_MEDIUM      = DIR_FONTS / 'JetBrainsMonoNL-Medium.ttf'
FONT_JET_BRAINS_MONO_NL_REGULAR     = DIR_FONTS / 'JetBrainsMonoNL-Regular.ttf'
FONT_JET_BRAINS_MONO_NL_SEMI_BOLD   = DIR_FONTS / 'JetBrainsMonoNL-SemiBold.ttf'
FONT_JET_BRAINS_MONO_NL_THIN        = DIR_FONTS / 'JetBrainsMonoNL-Thin.ttf'

FONT_SEGOE_UI_EMOJI = DIR_FONTS / 'Segoe-UI-Emoji.ttf'
