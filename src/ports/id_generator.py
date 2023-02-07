from abc import abstractmethod, ABC

class IId_generator(ABC):
    @abstractmethod
    def generate() -> str: 
        """Generate a random identifier"""
        pass
