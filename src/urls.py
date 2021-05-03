from flask_restful import Api

from src.handlers.address import AddressHandler
from src.handlers.delivery import DeliveryHandler
from src.handlers.health_check import HealthCheckHandler
from src.handlers.report import ReportHandler
from src.handlers.user import UserHandler


def init_resources(app):
    api = Api()
    api.add_resource(HealthCheckHandler, "/kikis-delivery-service/health-check")
    api.add_resource(DeliveryHandler, "/kikis-delivery-service/delivery")
    api.add_resource(AddressHandler, "/kikis-delivery-service/address")
    api.add_resource(UserHandler, "/kikis-delivery-service/user")
    api.add_resource(ReportHandler, "/kikis-delivery-service/report")
    api.init_app(app)
