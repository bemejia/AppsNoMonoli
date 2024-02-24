
from abc import ABC, abstractmethod

class Fabrica(ABC):
    @abstractmethod
    def crear_objeto(self, obj: any) -> any:
        ...