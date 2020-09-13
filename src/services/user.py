from src.queries import get_user_by_email, create_user


class UserService:

    @staticmethod
    def get_user_by_email(email):
        return get_user_by_email(email)

    @staticmethod
    def create_user(user: dict):
        create_user(user)
