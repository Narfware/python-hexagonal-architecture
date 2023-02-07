from abc import abstractmethod, ABC

from src.entities.order import Order

class Order_Repository(ABC):
    """Entity order database methods"""
    @abstractmethod
    def get_by_id(self, id: str) -> Order:
        """Retrieve an Order by id"""
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: str) -> list[Order]:
        """Retrieve an array of Orders by user id"""
        pass

    @abstractmethod
    def save(self, order: Order) -> None:
        """Save an Order in the database"""
        pass

    @abstractmethod
    def delete(self, order_id) -> None:
        """Delete an Order in the database"""
        pass

    @abstractmethod
    def update(self, order: Order) -> None:
        """Update an Order in the database"""
        pass
