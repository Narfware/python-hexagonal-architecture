from dependency_injector import containers, providers
from src.adapters.secondary.databases.mongo.main import Mongo_Client
from src.adapters.secondary.databases.mongo.order_repository import (
    Mongo_Order_Repository,
)
from src.adapters.secondary.identifiers.nanoid.main import Nano_id
from src.use_cases.order.create_order.main import Create_Order


class Container(containers.DeclarativeContainer):
    mongo_client = providers.Singleton(Mongo_Client().connect) # Inject database connection function

    ## REPOSITORIES
    order_repository = providers.Singleton(Mongo_Order_Repository, mongo_client) # Inject the database client connected

    ## ID GENERATOR
    id_generator = providers.Singleton(Nano_id) # Inject the database identifier generator

    create_order_use_case = providers.Factory( # Inject the use case with the necessary dependencies
        Create_Order,
        order_repository=order_repository,
        id_generator=id_generator,
    )
