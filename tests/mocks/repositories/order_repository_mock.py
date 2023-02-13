from entities.order import Order
from repositories.order_repository import Order_Repository


class Order_Repository_Mock(Order_Repository):
    def save(self, order: Order) -> None:
        raise Exception("Method invoked")

    def delete(self, order_id) -> None:
        raise Exception("Method invoked")

    def update(self, order: Order) -> None:
        raise Exception("Method invoked")

    def get_by_id(self, id: str) -> Order:
        raise Exception("Method invoked")

    def get_by_user_id(self, user_id: str) -> list[Order]:
        raise Exception("Method invoked")
