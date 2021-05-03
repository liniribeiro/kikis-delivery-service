from http import HTTPStatus

from flask import request
from flask_restful import Resource

from src.schemas.user_schema import DeliveryInput
from src.services.auth_service import requires_auth
from src.services.delivery import DeliveryService
from src.services.request_validation import validate


class DeliveryHandler(Resource):

    @requires_auth
    def get(self):
        user_id = request.values.get('user_id', None)
        id = request.values.get('id', None)
        response = DeliveryService().get_delivery(id, user_id)

        return response, HTTPStatus.OK

    @requires_auth
    @validate(DeliveryInput)
    def post(self):
        payload = request.json
        saved_id = DeliveryService().create_delivery(payload)
        return {"id": saved_id}, HTTPStatus.OK

