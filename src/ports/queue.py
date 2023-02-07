from abc import abstractmethod, ABC

class IQueue(ABC):
    @abstractmethod
    def publish(topic: str, message: str, attributes) -> None:
        """Publish a message"""
        pass
