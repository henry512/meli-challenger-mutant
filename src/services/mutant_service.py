from abc import ABC, abstractmethod
from injector import inject
from src.domains import DNAEntity, DNAStatisticsDto, DNAOriginEnum
from src.repositories import IMutantRepository
from src.infrastructure import IMemcachedContext
from typing import List, Optional

class IMutantService(ABC):
    @abstractmethod
    def save_dna(self, dna: DNAEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_dna(self, dna: List[str]) -> Optional[DNAEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_statistics(self) -> DNAStatisticsDto:
        raise NotImplementedError


class MutantService(IMutantService):
    @inject
    def __init__(self, repository: IMutantRepository, cache: IMemcachedContext):
        self._repository = repository
        self._cache = cache
        
    def save_dna(self, dna: DNAEntity) -> None:
        self._repository.save_dna(dna)

    def get_dna(self, dna: List[str]) -> Optional[DNAEntity]:
        dna_exists = self._repository.get_dna(dna)
        if dna_exists:
            return DNAEntity(
                sequence=dna_exists["sequence"],
                origin=dna_exists["origin"]
            )

    def get_statistics(self) -> DNAStatisticsDto:
        return DNAStatisticsDto(
            count_human_dna=100,
            count_mutant_dna=40,
            ratio=4.0
        )

