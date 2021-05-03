from http import HTTPStatus

from celery import current_app
from flask import request
from flask_restful import Resource

from src.celery_main import QUEUE_NAME
from src.services.auth_service import requires_auth


class ReportHandler(Resource):

    @requires_auth
    def post(self):
        data = request.json
        current_app.send_task("report",
                              args=[],
                              kwargs=data,
                              queue=QUEUE_NAME)

        return HTTPStatus.OK


