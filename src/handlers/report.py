from http import HTTPStatus

from celery import current_app
from flask import request
from flask_restful import Resource

from src.celery_main import QUEUE_NAME
from src.services.address import AddressService


class ReportHandler(Resource):

    def get(self, user_id):
        deliveries = AddressService().get_all_addresses(user_id)
        return deliveries, 200

    def post(self):
        data = request.json
        current_app.send_task("report",
                              args=[],
                              kwargs=data,
                              queue=QUEUE_NAME)

        return HTTPStatus.OK
