from http import HTTPStatus

from flask import request
from flask_restful import Resource

from src.database.models import Address
from src.database.queries import delete, get_by_id
from src.schemas.user_schema import AddressInput
from src.services.address import AddressService
from src.services.auth_service import requires_auth
from src.services.request_validation import validate


class AddressHandler(Resource):

    @requires_auth
    def get(self):
        user_id = request.values.get('user_id', None)
        id = request.values.get('id', None)
        response = AddressService().get_addresses(id, user_id)

        return response, HTTPStatus.OK

    @requires_auth
    @validate(AddressInput)
    def post(self):
        payload = request.json
        saved_id = AddressService().create_address(payload)
        return {"id": saved_id}, HTTPStatus.OK

    @requires_auth
    def delete(self):
        request_id = request.values.get('id')
        delete(Address, request_id)
        return HTTPStatus.OK
