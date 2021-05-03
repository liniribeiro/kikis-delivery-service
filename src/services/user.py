from typing import Text

from src.database.models import User
from src.database.queries import get_user_by_email, save, get_by_id, get_all


class UserService:

    @staticmethod
    def get_user(request_id: Text = None):
        if request_id:
            users = [get_by_id(User, request_id)]
        else:
            users = get_all(User)

        return users

    @staticmethod
    def get_user_by_email(email):
        return get_user_by_email(email)

    @staticmethod
    def save(user: dict):
        return save(User, user)
