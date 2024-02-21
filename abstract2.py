from abc import ABC,abstractmethod
                                 #abc - abstract base class
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tiers = n

    @abstractmethod
    def start(self):
        pass

