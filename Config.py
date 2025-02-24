
import dotenv
import os

env = dotenv.dotenv_values('.env')

# Project config
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

# Assets config
FONTS_DIR = os.path.join(PROJECT_DIR, 'Gui', 'Fonts')

# Logging config
LOG_LVL = env.get('LOG_LVL', 'CRITICAL')
LOG_FILE = env.get('LOG_FILE', None)
LOG_FMT = env.get('LOG_FMT', '%(asctime)s %(levelname)s %(message)s')
