from abc import ABC, abstractmethod
from typing import Any, Dict
from injector import inject
from src.domains import DNAEntity
from src.infrastructure import IPostgresContext


class IMutantRepository(ABC):
    @abstractmethod
    def save_dna(self, dna: DNAEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_dna(self, key: str) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_statistics(self) -> Dict[str, int]:
        raise NotImplementedError


class MutantRepository(IMutantRepository):
    @inject
    def __init__(self, context: IPostgresContext):
        self._context = context

    def save_dna(self, dna: DNAEntity) -> None:
        print("save dna repository")

    def get_dna(self, key: str) -> Dict[str, Any]:
        return {
            "id": "1",
            "sequence": ["ADN"],
            "origin": "HUMAN"
        }

    def get_statistics(self) -> Dict[str, int]:
        return {
            "mutan": 0,
            "human": 0
        }

