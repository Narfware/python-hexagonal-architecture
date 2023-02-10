from src.entities.order import Order
from src.repositories.order_repository import Order_Repository
from src.adapters.secondary.tracing.open_telemetry.decorator import instrument
from pymongo import MongoClient


@instrument
class Mongo_Order_Repository(Order_Repository):
    def __init__(self, client: MongoClient) -> None:
        self.client = client
        self.collection = "orders"

    def save(self, order: Order) -> None:
        self.client.get_database().get_collection(self.collection).insert_one(
            order.__dict__
        )

    def delete(self, order_id) -> None:
        self.client.get_database().get_collection(self.collection).delete_one(
            {"_id": order_id}
        )

    def update(self, order: Order) -> None:
        self.client.get_database().get_collection(self.collection).update_one(
            {"_id": order["_id"]}, {"$set": order.__dict__}
        )

    def get_by_id(self, id: str) -> Order:
        result = (
            self.client.get_database()
            .get_collection(self.collection)
            .find_one({"_id": id})
        )
        return Order(result) if result != None else None

    def get_by_user_id(self, user_id: str) -> list[Order]:
        results = list(
            self.client.get_database()
            .get_collection(self.collection)
            .find({user_id: user_id})
        )
        return list(map(lambda order: Order(**order), results))
