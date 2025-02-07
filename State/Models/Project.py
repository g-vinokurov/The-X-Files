
import pathlib

from State.Models.Report import Report

from Logger import log


class Project:
    def __init__(self, dir: str):
        self._dir = dir
        self._reports = []
        self._load()
    
    @property
    def dir(self):
        return self._dir
     
    @property
    def reports(self):
        return self._reports
    
    def _load(self):
        project_dir = pathlib.Path(self._dir).resolve()

        if not project_dir.is_absolute():
            project_dir = pathlib.Path.cwd() / project_dir
        log.debug(f'Load reports from {project_dir}')
        
        if not project_dir.exists():
            msg = f'Path {project_dir} not found'
            log.error(msg)
            raise FileNotFoundError(msg)
        
        for entity in project_dir.iterdir():
            if not entity.is_dir():
                continue
            try:
                report = Report(entity)
            except Exception as err:
                log.error(f'{err}')
                continue
            self._reports.append(report)
        return
