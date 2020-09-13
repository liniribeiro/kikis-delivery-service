from flask import request
from flask_restful import Resource

from src.services.delivery import DeliveryService


class DeliveryHandler(Resource):

    def get(self):
        deliveries = DeliveryService().get_all_deliveries()
        return deliveries, 200

    def post(self):
        data = request.json
        DeliveryService().create_delivery(data)
        return {}, 200
