
from abc import ABC, abstractmethod

class Endpoint(ABC):

    @abstractmethod
    def call(self, prompt):
        pass
