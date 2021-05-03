from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database.models.base import BaseModel


class Address(BaseModel):
    __tablename__ = 'address'

    cep = Column(String)
    road = Column(String)
    state = Column(String)
    city = Column(String)
    complement = Column(String)

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates="address")

    def __repr__(self):
        return f'Adrress {self.road}, {self.complement}, {self.city}, {self.state} - {self.cep}.'

    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id),
            'cep': str(self.cep),
            'road': str(self.road),
            'state': str(self.state),
            'city': str(self.city),
            'complement': str(self.complement),
        }