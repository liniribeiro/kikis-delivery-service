from src.database.models import Address
from src.database.queries import get_all_user_addresses, save, get_by_id


class AddressService:

    @staticmethod
    def get_addresses(id=None, user_id=None):
        if user_id:
            return get_all_user_addresses(user_id)
        else:
            return [get_by_id(Address, id)]

    @staticmethod
    def create_address(address: dict):
        return save(Address, address)

