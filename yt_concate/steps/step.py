from abc import ABC
from abc import abstractmethod
class Step(ABC):
    def __init__(self):
        pass
    @abs
    def process(self, inputs):
        pass
class StepException(Exception):
    pass


