
import pathlib

from State.Models.Report import Report

from Log import log


class ReportLoader:
    @classmethod
    def load(cls, path_to_report_dir: str) -> Report:
        report_dir = pathlib.Path(path_to_report_dir).resolve()

        if not report_dir.is_absolute():
            report_dir = pathlib.Path.cwd() / report_dir
        log.debug(f'Load report from {report_dir}')
        
        if not report_dir.exists():
            raise FileNotFoundError(f'Path {report_dir} not found')
        
        report_file_path = report_dir / 'report.json'
        if not report_file_path.exists():
            raise FileNotFoundError(f'{report_dir.name}: File report.json not found, skipped!')
        
        with open(report_file_path, 'r', encoding='utf-8') as report_file:
            report_data = report_file.read()
        
        report = Report.model_validate_json(report_data)
        
        return report
