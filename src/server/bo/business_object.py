from abc import ABC #, abstractmethod

class BusinessObject(ABC):
    def __init__(self):
        self._id = 0

    def get_id(self) -> int:
        return self._id

    def set_id(self, value: int):
        self._id = value