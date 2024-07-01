from abc import ABC, abstractmethod
import pickle


class DAO(ABC):

    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, object):
        self.__cache[key] = object
        self.__dump()

    def get(self, key):
        return self.__cache.get(key)

    def remove(self, key):
        try:
            del self.__cache[key]
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return list(self.__cache.values())

    def get_size(self):
        return int(len(list(self.__cache.values())))

    def atualiza(self):
        self.__dump()
    
