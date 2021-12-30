from abc import ABC, abstractmethod
from typing import Any, Dict
from src.domains import DNAEntity


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

