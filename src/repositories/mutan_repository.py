from abc import ABC, abstractmethod
from typing import Any, Dict
from injector import inject
from pypika.queries import QueryBuilder
from src.domains import DNAEntity, DNAOriginEnum
from src.infrastructure import IPostgresContext
from pypika import PostgreSQLQuery as Query, Table, functions as fn
from src.config import IConfiguration
from psycopg2.errors import UniqueViolation
from pandas import DataFrame


class IMutantRepository(ABC):
    @abstractmethod
    def save_dna(self, dna: DNAEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_statistics(self) -> Dict[str, int]:
        raise NotImplementedError


class MutantRepository(IMutantRepository):
    @inject
    def __init__(self, context: IPostgresContext, configuration: IConfiguration):
        self._context = context
        self._config = configuration.config
        self._table = Table(self._config["DATABASE_TABLE_DNA"])

    def save_dna(self, dna: DNAEntity) -> None:
        dna_sequence: str = "-".join(dna["sequence"])
        dna_origin: str = dna["origin"].value

        query: QueryBuilder = (
            Query.into(self._table)
            .columns(self._table.sequence, self._table.origin)
            .insert(dna_sequence, dna_origin)
        )
        try:
            self._context.execute_query(query.get_sql())
        except UniqueViolation:
            return

    def get_statistics(self) -> Dict[str, int]:
        query: QueryBuilder = (
            Query.from_(self._table)
            .select(
                (fn.Count("*")).as_("count_dna"),
                self._table.origin,
            )
            .groupby(
                self._table.origin,
            )
        )

        data_stats: Dict[str, Any] = {
            "mutant": 0,
            "human": 0,
            "ratio": 0.0
        }

        result: DataFrame = self._context.find(query.get_sql())
        if not result.empty:
            mutant_count_dna = result["count_dna"][result["origin"] == DNAOriginEnum["MUTANT"].value]
            human_count_dna = result["count_dna"][result["origin"] == DNAOriginEnum["HUMAN"].value]

            data_stats["human"] = int(human_count_dna) if not human_count_dna.empty else 0
            data_stats["mutant"] = int(mutant_count_dna) if not mutant_count_dna.empty else 0
            try:
                data_stats["ratio"] = round(data_stats["human"] / data_stats["mutant"], 2)
            except ZeroDivisionError:
                data_stats["ratio"] = 0.0

        return data_stats

