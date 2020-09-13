import factory
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from src.models import DeclarativeBase, User

engine = create_engine('sqlite:///:memory:')
Session = scoped_session(sessionmaker())
DeclarativeBase.metadata.create_all(engine)


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope='function')
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    UserFactory._meta.sqlalchemy_session = session
    yield session
    session.close()
    transaction.rollback()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    name = factory.Faker('name')
    password = factory.Faker('password')

    class Meta:
        model = User


def my_func_to_delete_user(session, user_id):
    session.query(User).filter(User.id == user_id).delete()


def test(session):
    mock_user = UserFactory.create()
    assert session.query(User).one()

    my_func_to_delete_user(session, mock_user.id)

    result = session.query(User).one_or_none()
    assert result is None

    mock_user = UserFactory.create_batch(50)
    result = session.query(User).count()
    assert result is 50
    print(mock_user)
