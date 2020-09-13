from src.queries import get_all_deliveries, create_delivery


class DeliveryService:

    @staticmethod
    def get_all_deliveries():
        return get_all_deliveries()

    @staticmethod
    def create_delivery(delivery: dict):
        delivery.update({
            'status': 'in_queue',
            'price': 34.66
        })
        create_delivery(delivery)
