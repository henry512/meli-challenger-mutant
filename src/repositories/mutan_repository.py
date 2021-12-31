from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from injector import inject
from src.domains import DNAEntity
from src.infrastructure import IPostgresContext
from src.utils import encode_data, decode_data
from pypika import PostgreSQLQuery as Query, Table
from src.config import IConfiguration
from psycopg2.errors import UniqueViolation
from pandas import DataFrame


class IMutantRepository(ABC):
    @abstractmethod
    def save_dna(self, dna: DNAEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_dna(self, dna: List[str]) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def get_statistics(self) -> Dict[str, int]:
        raise NotImplementedError


class MutantRepository(IMutantRepository):
    @inject
    def __init__(self, context: IPostgresContext, configuration: IConfiguration):
        self._context = context
        self._config = configuration.config

    def save_dna(self, dna: DNAEntity) -> None:
        dna_sequence: str = encode_data("-".join(dna["sequence"]))
        dna_origin: str = dna["origin"].value

        query = Query \
            .into(Table(self._config["DATABASE_TABLE_DNA"])) \
                .columns("sequence", "origin")\
                .insert(dna_sequence, dna_origin)
        try:
            self._context.execute_query(query.get_sql())
        except UniqueViolation:
            return
        

    def get_dna(self, dna: List[str]) -> Optional[Dict[str, Any]]:
        dna_sequence: str = encode_data("-".join(dna))

        table = Table(self._config["DATABASE_TABLE_DNA"])
        query = Query \
            .from_(table) \
            .select(table.sequence,
                    table.origin) \
            .where((table.sequence == dna_sequence))

        dna_exists: DataFrame = self._context.find(query.get_sql())
        if not dna_exists.empty:
            return {
                "sequence": decode_data(dna_exists["sequence"][0]).split("-"),
                "origin": dna_exists["origin"][0]
            }

    def get_statistics(self) -> Dict[str, int]:
        return {
            "mutan": 0,
            "human": 0
        }

