from flask import request
from flask_restful import Resource

from src.services.user import UserService


class UserHandler(Resource):

    def get(self, email):
        user = UserService().get_user_by_email(email)
        return user, 200

    def post(self):
        data = request.json
        UserService().create_user(data)
        return {}, 200
