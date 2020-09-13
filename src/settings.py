import os

from decouple import config

TEST = config('TEST')

DB_URI = config('DB_URI')

BASE_DIR = os.path.dirname(os.path.dirname( os.path.abspath(__file__)))

HOST = config('HOST', default='0.0.0.0')
PORT = config('PORT', cast=int, default=7000)
DEBUG = config('DEBUG', default=False)


CELERY = {
    "BROKER_URL": config('CELERY_BROKER_URL'),
    "RESULT_BACKEND": config('CELERY_RESULT_BACKEND'),
    "task_always_eager": False,
    "CELERY_TIMEZONE": "America/Sao_Paulo",
    "CELERY_ENABLE_UTC": True,
}

ELASTIC_APM = {
    'SERVICE_NAME': f"kikis-delivery-service",
    'SERVICE_VERSION': 1,
    'COLLECT_LOCAL_VARIABLES': 'all',
    'ELASTIC_APM_SERVER_URL': config('ELASTIC_APM_SERVER_URL'),
    'ELASTIC_APM_CAPTURE_BODY': 'all',
    'CAPTURE_BODY': 'all'
}
