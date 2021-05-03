from itertools import islice
from typing import Dict, List, cast, Text

from sqlalchemy import func, String
from sqlalchemy.dialects.postgresql import ARRAY

from src.apm.apm_decorator import apm_capture_span
from src.database.db_connection import DBConnector
from src.database.models import Delivery, Address
from src.database.models.user import User


def get_all_user_addresses(user_id) -> List[Address]:
    with DBConnector().conn_session() as session:
        addresses = session.query(Address).filter_by(user_id=user_id).all()
        return [address.to_dict() for address in addresses]


def get_user_by_email(email: str) -> Dict:
    with DBConnector().conn_session() as session:
        user = session.query(User).filter_by(email=email).first()
        return user.to_dict()


def get_all_deliveries_by_user(user_id) -> List[Dict]:
    with DBConnector().conn_session() as session:
        deliveries = session.query(Delivery).filter_by(user_id=user_id).all()
        return [delivery.to_dict() for delivery in deliveries]


def split_generics(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))


@apm_capture_span
def get_resume_query(session):


    user_data = func.array_agg(func.row(User.id, User.name)).label('user')
    query = session.query(
        Delivery.status,
        Address.city,
        user_data). \
        join(User, Delivery.user_id == User.id). \
        join(Address, Delivery.user_id == Address.user_id)

    deliveries = query.group_by(Delivery.status, Address.city)
    return deliveries


def get_delivery_report():
    with DBConnector().conn_session() as session:
        query = get_resume_query(session)
        chunk = query.yield_per(1000)
        return split_generics(500, chunk)


def delete(db_model, object_id):
    with DBConnector().conn_session() as session:
        db_object = session.query(db_model).filter_by(id=object_id).first()
        session.delete(db_object)


def save(db_model, dict_object):
    with DBConnector().conn_session() as session:
        object_class = db_model(**dict_object)
        session.add(object_class)
        session.flush()
        return str(object_class.id)


def get_all(db_model):
    with DBConnector().conn_session() as session:
        db_object = session.query(db_model).all()
        return [c.to_dict() for c in db_object]


def get_by_id(db_model, object_id: Text):
    with DBConnector().conn_session() as session:
        db_object = session.query(db_model).filter_by(id=object_id).first()
        return db_object.to_dict()