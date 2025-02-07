
import pathlib
import bs4
import secrets
import datetime

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
        
        report_file_path = report_dir / 'report.xml'
        if not report_file_path.exists():
            msg = 'File report.xml not found, skipped!'
            log.error(msg)
            raise FileNotFoundError(msg)
        
        # log.info(f'Report "{report_name}" loaded')
    
    def __parse_report(self, report_file_path: str):
        # with open(report_file_path, 'r') as report_file:
        #     report_xml = bs4.BeautifulSoup(report_file.read(), 'xml')
        # 
        # report_head = report_xml.find('head', recursive=False)
        # if report_head is None:
        #     msg = 'Report Head not found, skipped!'
        #     log.error(msg)
        #     raise ValueError(msg)
        # 
        # report_name = report_head.find('name', recursive=False)
        # if report_name is not None:
        #     report_name = str(report_name.text).strip()
        # else:
        #     report_name = secrets.token_hex(16)
        #     log.warning('Report name is not defined: generated random')
        # log.debug(f'Report Name: {report_name}')
        # 
        # report_provider = report_head.find('provider', recursive=False)
        # if report_provider is not None:
        #     report_provider = str(report_provider.text).strip()
        # else:
        #     log.warning('Report provider is not defined')
        # log.debug(f'Report Provider: {report_provider}')
# 
        # report_type = report_head.find('type', recursive=False)
        # if report_type is not None:
        #     report_type = str(report_type.text).strip()
        # else:
        #     log.warning('Report type is not defined')
        # log.debug(f'Report Type: {report_type}')
        # 
        # report_date = report_head.find('date', recursive=False)
        # if report_date is not None:
        #     report_date = str(report_date.text).strip()
        # try:
        #     report_date = datetime.datetime.strptime(report_date, "%d.%m.%Y").date()
        # except Exception:
        #     log.warning('Report date is undefined or incorrect')
        # log.debug(f'Report Date: {report_date}')
# 
        # report_level = report_head.find('level', recursive=False)
        # if report_level is not None:
        #     report_level = str(report_level.text).strip()
        # else:
        #     log.warning('Report level is not defined')
        # log.debug(f'Report Level: {report_level}')
# 
        # report_tags = report_head.find('tags', recursive=False)
        # if report_tags is not None:
        #     report_tags = report_tags.find_all('tag', recursive=False)
        # else:
        #     report_tags = []
        # for i in range(len(report_tags)):
        #     report_tags[i] = str(report_tags[i].text).strip()
        # log.debug(f'Report Tags: {", ".join(report_tags)}')
# 
        # report_body = report_xml.find('body', recursive=False)
        # if report_body is None:
        #     msg = 'Report Body not found, skipped!'
        #     log.error(msg)
        #     raise ValueError(msg)
        # 
        # report_task = report_body.find('task', recursive=False)
        # if report_task is None:
        #     msg = 'Report Task not found, skipped!'
        #     log.error(msg)
        #     raise ValueError(msg)
        # 
        # report_solution = report_body.find('solution', recursive=False)
        # if report_solution is None:
        #     msg = 'Report Solution not found, skipped!'
        #     log.error(msg)
        #     raise ValueError(msg)
        pass
