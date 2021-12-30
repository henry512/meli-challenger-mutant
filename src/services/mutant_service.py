from abc import ABC, abstractmethod
from injector import inject
from src.domains import DNAEntity
from src.domains import DNAStatisticsDto
from src.domains import DNAOriginEnum
from src.repositories import IMutantRepository


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
    def __init__(self, repository: IMutantRepository):
        self._repository = repository
        
    def save_dna(self, dna: DNAEntity) -> None:
        print("save dna repository")

    def get_dna(self, key: str) -> DNAEntity:
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

