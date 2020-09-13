from itertools import islice
from typing import Dict, List, cast

from sqlalchemy import func, String
from sqlalchemy.dialects.postgresql import ARRAY

from src.apm.apm_decorator import apm_capture_span
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


def get_all_user_addresses(user_id) -> User:
    with DBConnector().conn_session() as session:
        user = session.query(User).filter_by(user_id=user_id).all()
        return user.to_dict()


def get_user_by_email(email: str) -> Dict:
    with DBConnector().conn_session() as session:
        user = session.query(User).filter_by(email=email).first()
        return user.to_dict()


def get_all_deliveries() -> List[Dict]:
    with DBConnector().conn_session() as session:
        deliveries = session.query(Delivery).all()
        return [delivery.to_dict() for delivery in deliveries]


def split_generics(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))


@apm_capture_span
def get_resume_query(session):
    user_data = cast(func.array_agg(func.row(User.id,
                                             User.name)), ARRAY(String))

    query = session.query(
        Delivery.status,
        Address.city,
        user_data.label('user')). \
        join(User, Delivery.user_id == User.id). \
        join(Address, Delivery.user_id == Address.user_id)

    deliveries = query.group_by(Delivery.status, Address.city)
    return deliveries


def get_delivery_report():
    with DBConnector().conn_session() as session:
        query = get_resume_query(session)
        chunk = query.yield_per(1000)
        return split_generics(500, chunk)
