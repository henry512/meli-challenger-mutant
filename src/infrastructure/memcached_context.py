from abc import ABC, abstractmethod
from typing import Any
from injector import inject
from src.config import IConfiguration
from logging import getLogger
from retry import retry
from pymemcache.client.base import Client, MemcacheUnexpectedCloseError

from src.utils import CacheJsonSerde


class IMemcachedContext(ABC):
    @abstractmethod
    def get(self, key: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def set(self, key: str, data: Any):
        raise NotImplementedError


class MemcachedContext(IMemcachedContext):
    @inject
    def __init__(self, configuration: IConfiguration):
        self._configuration = configuration.config
        self._cache_host = self._configuration["CACHE_HOST"]
        self._cache_port = self._configuration["CACHE_PORT"]
        self._cache_exp_time = self._configuration["CACHE_EXPIRATION_TIME"]
        self._connection: Client = None

    def get(self, key: str) -> str:
        cnx = self._get_connection()
        try:
            return cnx.get(key)
        except Exception as error:
            print(f"Memcached Exception has occurred: \n Error: {error} \n Key: {key} \n")
            raise

    def set(self, key: str, data: Any):
        cnx = self._get_connection()
        try:
            cnx.set(key, data, expire=self._cache_exp_time)
        except Exception as error:
            print(f"Memcached Exception has occurred: \n Error: {error} \n Key: {key} \n")
            raise

    def _get_connection(self) -> Any:
        if self._connection is None:
            self._open_connection()
        return self._connection

    @retry((MemcacheUnexpectedCloseError), tries=3, logger=getLogger(__name__))
    def _open_connection(self) -> Any:
        try:
            self._connection = Client(
                (self._cache_host , self._cache_port), serde=CacheJsonSerde()
            )
        except MemcacheUnexpectedCloseError:
            raise
