from functools import wraps
from http import HTTPStatus
from typing import Type, Dict, List

from flask import request
from schematics import Model
from schematics.exceptions import DataError

from src.exceptions import PayloadError


def validate(request_class: Type[Model] = None):
    def internal_validate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            body = request.json
            if request_class:
                try:
                    request_class(body).validate()
                    return fn(*args, **kwargs)
                except DataError as e:
                    return PayloadError(error=str(e)).to_dict(), HTTPStatus.INTERNAL_SERVER_ERROR
        return wrapper
    return internal_validate
