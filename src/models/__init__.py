from src.models.base import DeclarativeBase
from src.models.user import User
from src.models.address import Address
from src.models.delivery import Delivery

__all__ = ["User", "DeclarativeBase", "Address", "Delivery"]

"""
Um usuário pode ter várias entregas vínculadas a ele
"""