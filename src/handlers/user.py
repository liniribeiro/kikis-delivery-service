from http import HTTPStatus

from flask import request
from flask_restful import Resource

from src.database.models import User
from src.database.queries import delete
from src.schemas.user_schema import UserInput
from src.services.auth_service import requires_auth
from src.services.request_validation import validate
from src.services.user import UserService


class UserHandler(Resource):

    @requires_auth
    def get(self):
        id = request.values.get('id', None)
        email = request.values.get('email', None)

        if email:
            response = UserService().get_user_by_email(email)
        else:
            response = UserService().get_user(id)
        return response, HTTPStatus.OK

    @requires_auth
    @validate(UserInput)
    def post(self):
        payload = request.json
        saved_id = UserService().save(payload)
        return {"id": saved_id}, HTTPStatus.OK

    @requires_auth
    def delete(self):
        request_id = request.values.get('id')
        delete(User, request_id)
        return HTTPStatus.OK
