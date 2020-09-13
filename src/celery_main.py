from celery import Celery
from celery.signals import import_modules

from src.apm.apm_config import ApmClient
from src.settings import CELERY, ELASTIC_APM

from src.tasks.report import ReportTasK

QUEUE_NAME = 'kikis-delivery-service'
celery_app = Celery(QUEUE_NAME, config_source=CELERY)
ApmClient().initialize(ELASTIC_APM)


@import_modules.connect
def import_modules(*args, **kwargs):
    celery_app.register_task(ReportTasK())