from flask import request
from flask_restful import Resource

from src.services.address import AddressService


class AddressHandler(Resource):

    def get(self, user_id):
        deliveries = AddressService().get_all_addresses(user_id)
        return deliveries, 200

    def post(self):
        data = request.json
        AddressService().create_address(data)
        return {}, 200
