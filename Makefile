PKG_NAME := src
PYTHONPATH := $(shell pwd)

run_gunicorn:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" gunicorn -c ./src/gunicorn.py src.main:app

run_celery:
	@echo "---- Running Celery ----"
	@PYTHONPATH="${PYTHONPATH}" celery -A src.celery_main.celery_app worker -l info -P gevent -n kikis-delivery-service-worker@%n --autoscale=1,1 -Q kikis-delivery-service

run_all:
	@echo "---- Running Application + Celery ----"
	@make run_gunicorn & make run_celery