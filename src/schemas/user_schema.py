

from schematics import Model
from schematics.types import StringType, FloatType, ListType, ModelType


class UserInput(Model):
    name = StringType()
    password = StringType()
    email = StringType()


class DeliveryInput(Model):
    delivery_address_id = StringType()
    pick_up_address_id = StringType()
    delivery_date = StringType()
    pick_up_date = StringType()
    package_weight = FloatType()
    user_id = StringType()


class AddressInput(Model):
    cep = StringType()
    road = StringType()
    state = StringType()
    city = StringType()
    complement = StringType()
    user_id = StringType()


class UserOutput(Model):
    name = StringType()
    email = StringType()
    deliveries = ListType(ModelType(DeliveryInput))
    addresses = ListType(ModelType(AddressInput))

#
# def get_user_output(company_dict):
#     mapped_output = [CompanyOutput(comp) for comp in company_dict]
#     schema = CompanyOutputList()
#     schema.companies = mapped_output
#     return schema
