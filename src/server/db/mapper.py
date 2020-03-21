import mysql.connector as connector
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod

class Mapper(AbstractContextManager, ABC):

    def __init__(self):
        self._cnx = None

    def __enter__(self):
        self._cnx = connector.connect(user='demo', password='demo',
                              host='127.0.0.1',
                              database='homework-io')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cnx.close()

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_key(self, key):
        pass

    @abstractmethod
    def insert(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass