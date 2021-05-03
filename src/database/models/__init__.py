from src.database.models.address import Address
from src.database.models.delivery import Delivery
from src.database.models.base import DeclarativeBase
from src.database.models.user import User

__all__ = ["User", "DeclarativeBase", "Address", "Delivery"]

"""
Um usuário pode ter várias entregas vínculadas a ele
"""