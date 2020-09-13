
from celery import Task

from src.services.delivery_report import ReportService


class ReportTasK(Task):
    name = 'report'

    def run(self, *args, **kwargs):
        ReportService().process_report()

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        pass
