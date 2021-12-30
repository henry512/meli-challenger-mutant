from abc import ABC, abstractmethod
from injector import inject
from src.domains import DNAEntity, DNAStatisticsDto, DNAOriginEnum
from src.repositories import IMutantRepository
from src.infrastructure import IMemcachedContext

class IMutantService(ABC):
    @abstractmethod
    def save_dna(self, dna: DNAEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_dna(self, key: str) -> DNAEntity:
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
        print("save dna repository")

    def get_dna(self, key: str) -> DNAEntity:
        self._repository.get_dna("key")
        return DNAEntity(
            sequence=["DNA"],
            origin=DNAOriginEnum.HUMAN.value
        )

    def get_statistics(self) -> DNAStatisticsDto:
        return DNAStatisticsDto(
            count_human_dna=100,
            count_mutant_dna=40,
            ratio=4.0
        )

