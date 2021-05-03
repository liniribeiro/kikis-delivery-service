import logging
from functools import wraps
from http import HTTPStatus

from flask import request

from src.exceptions import AuthenticationError
from src.settings import API_KEY


def requires_auth(func):

    @wraps(func)
    def wrapper(*args):
        api_key = request.headers.get('Authorization')

        if api_key != API_KEY:
            return AuthenticationError().to_dict(), HTTPStatus.UNAUTHORIZED
        else:
            logging.info(f"Autenticação autorizada!")
        return func(*args)

    return wrapper
