from abc import ABC, abstractmethod
from pyms.flask.app import config


class IConfiguration(ABC):
    @abstractmethod
    def config(self, keys):
        raise NotImplementedError


class Configuration(IConfiguration):
    def __init__(self):
        self.__config = config()

    @property
    def config(self):
        return self.__config