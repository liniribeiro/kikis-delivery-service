from typing import Dict, List

from src.migrations.upgrade import upgrade
from src.db_connection import DBConnector
from src.models import Delivery, Address
from src.models.user import User


def create_user(user: Dict):
    with DBConnector().conn_session() as session:
        user_object = User(**user)
        session.add(user_object)


def create_delivery(delivery: Dict):
    with DBConnector().conn_session() as session:
        delivery_object = Delivery(**delivery)
        session.add(delivery_object)


def create_address(address: Dict):
    with DBConnector().conn_session() as session:
        address_object = Address(**address)
        session.add(address_object)
        return address_object.id


def get_user_by_email(email: str) -> Dict:
    with DBConnector().conn_session() as session:
        user = session.query(User).filter_by(email=email).first()
        return user.to_dict()


def get_all_deliveries() -> User:
    with DBConnector().conn_session() as session:
        return session.query(Delivery).all()
