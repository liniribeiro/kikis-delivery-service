from src.queries import create_address, get_all_user_addresses


class AddressService:

    @staticmethod
    def get_all_addresses(user_id):
        return get_all_user_addresses(user_id)

    @staticmethod
    def create_address(address: dict):
        create_address(address)
