from src.adapters.secondary.databases.mongo.main import Mongo_Client
from src.adapters.secondary.databases.mongo.order_repository import Mongo_Order_Repository
from src.adapters.secondary.identifiers.nanoid.main import Nano_id
from src.adapters.primary.http.fast_api.main import FastApiManager
from src.use_cases.order.create_order.main import Create_Order

def main():
    mongo_client = Mongo_Client().connect()

    mongo_order_repository = Mongo_Order_Repository(mongo_client)

    create_order_use_case = Create_Order(mongo_order_repository, Nano_id())

    return FastApiManager(create_order_use_case).initialize()

main()

