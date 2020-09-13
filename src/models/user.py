
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    delivery = relationship("Delivery", cascade="all,delete", back_populates="user")
    address = relationship("Address", cascade="all,delete", back_populates="user")

    def __repr__(self):
        return f'User {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id)
        }
