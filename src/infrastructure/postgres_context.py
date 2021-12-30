from abc import ABC, abstractmethod
from injector import inject
import psycopg2
from typing import Any, List
from logging import getLogger
from retry import retry
from pandas import DataFrame
from src.config import IConfiguration


class IPostgresContext(ABC):
    @abstractmethod
    def find(self, query: str) -> DataFrame:
        raise NotImplementedError

    @abstractmethod
    def execute_query(self, query: str) -> None:
        raise NotImplementedError


class PostgresContext(IPostgresContext):
    @inject
    def __init__(self, configuration: IConfiguration):
        self._configuration: Any = configuration.config
        self.connectionstring: str = self._configuration["CONNECTION_DATABASE"]
        self._connection: Any = None

    def __del__(self) -> None:
        if (self._connection is not None) and (not self._connection.closed):
            self._connection.close()

    def find(self, query: str) -> DataFrame:
        with self._get_connection() as cnx:
            with cnx.cursor() as cursor:
                try:
                    cursor.execute(query)
                    result: Any = cursor.fetchall()
                    columns: List[str] = [columns.name for columns in cursor.description]
                    return DataFrame(result, columns=columns)
                except Exception:
                    if cursor is not None:
                        cnx.rollback()
                    print(f"Postgres Exception has occurred: \n Query: {query} \n")
                    raise

    def execute_query(self, query: str) -> None:
        with self._get_connection() as cnx:
            with cnx.cursor() as cursor:
                try:
                    cursor.execute(query)
                    cnx.commit()
                except Exception:
                    if cursor is not None:
                        cnx.rollback()
                    print(f"Postgres Exception has occurred: \n Query: {query} \n")
                    raise

    def _get_connection(self) -> Any:
        if self._connection is None or self._connection.closed:
            self._open_connection()
        return self._connection

    @retry((psycopg2.OperationalError), tries=3, logger=getLogger(__name__))
    def _open_connection(self) -> Any:
        try:
            self._connection = psycopg2.connect(self.connectionstring)
        except psycopg2.OperationalError:
            raise
