
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

FONTS_DIR = os.path.join(PROJECT_DIR, 'Gui', 'Fonts')
ICONS_DIR = os.path.join(PROJECT_DIR, 'Gui', 'Icons')

LOG_LVL = 'DEBUG'
LOG_FILE = None
LOG_FMT = '%(asctime)s %(levelname)s %(message)s'

DB_URL = 'sqlite+pysqlite:///:memory:'
DB_ECHO = LOG_LVL == 'DEBUG'
