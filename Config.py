
import dotenv
import pathlib

env = dotenv.dotenv_values('.env')

# Project root path
DIR_ROOT = pathlib.Path(__file__).absolute().parent

# Assets paths
DIR_ASSETS = DIR_ROOT / 'Ui' / 'Assets'
DIR_FONTS = DIR_ASSETS / 'Fonts'
DIR_ICONS = DIR_ASSETS / 'Icons'

# Logging config
LOG_LVL = env.get('LOG_LVL', 'CRITICAL')
LOG_FILE = env.get('LOG_FILE', None)
LOG_FMT = env.get('LOG_FMT', '%(asctime)s %(levelname)s %(message)s')
