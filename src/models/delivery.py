from enum import Enum

from sqlalchemy import Column, String, ForeignKey, DateTime, Enum as EnumSqlAlchemy, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class DeliveryStatus(Enum):
    in_queue = 'in_queue'
    in_progress = 'in_progress'
    delivered = 'delivered'


class Delivery(BaseModel):
    __tablename__ = 'delivery'

    delivery_address_id = Column(UUID(as_uuid=True), ForeignKey('address.id'), nullable=False)
    pick_up_address_id = Column(UUID(as_uuid=True), ForeignKey('address.id'), nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    pick_up_date = Column(DateTime, nullable=False)
    status = Column(EnumSqlAlchemy(DeliveryStatus), nullable=True)
    price = Column(Float)

    package_weight = Column(Float)

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates="delivery")

    def __repr__(self):
        return f'Delivery'


