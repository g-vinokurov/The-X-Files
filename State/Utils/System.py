
import os
import sys


class System:
    @classmethod
    def get_path_to_home(cls):
        if sys.platform == 'win32':
            return os.path.join(os.environ['USERPROFILE'])
        if sys.platform == 'linux':
            return os.path.join(os.path.expanduser('~'))
        raise RuntimeError(f'Unsupported platform: {sys.platform}')
    
    @classmethod
    def get_path_to_desktop(cls):
        path_to_home = cls.get_path_to_home()
        path_to_desktop = os.path.join(path_to_home, 'Desktop')
        return path_to_desktop
