PKG_NAME := src
PYTHONPATH := $(shell pwd)

run_gunicorn:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" gunicorn -c ./src/gunicorn.py src.app:app

run_celery:
	@echo "---- Running Celery ----"
	@PYTHONPATH="${PYTHONPATH}" celery worker -A src.celery_app.celery_app -l info -P gevent -n kikis-delivery-service-worker@%n --autoscale=1,1 -Q kikis-delivery-service

run_all:
	@echo "---- Running Application + Celery ----"
	@make run_gunicorn & make run_celery