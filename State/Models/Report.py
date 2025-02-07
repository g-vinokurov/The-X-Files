
import pathlib

from Logger import log


class Report:
    def __init__(self, dir: str):
        self._dir = dir
        self._name = 'Untitled'
        self._load()
    
    @property
    def dir(self):
        return self._dir
    
    @property
    def name(self):
        return self._name
    
    def _load(self):
        report_dir = pathlib.Path(self._dir).resolve()

        if not report_dir.is_absolute():
            report_dir = pathlib.Path.cwd() / report_dir
        log.debug(f'Load report from {report_dir}')
        
        if not report_dir.exists():
            msg = f'Path {report_dir} not found'
            log.error(msg)
            raise FileNotFoundError(msg)
        
        self._name = report_dir.name
        log.info(f'Report {self._name} loaded')
