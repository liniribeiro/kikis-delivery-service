from src.database.models import Delivery
from src.database.queries import save, get_by_id, get_all, get_all_deliveries_by_user


class DeliveryService:

    @staticmethod
    def get_delivery(id, user_id):
        if user_id:
            return get_all_deliveries_by_user(user_id)
        elif id:
            return [get_by_id(Delivery, id)]
        else:
            return get_all(Delivery)

    @staticmethod
    def create_delivery(delivery: dict):
        delivery.update({
            'status': 'in_queue',
            'price': 34.66
        })
        return save(Delivery, delivery)

