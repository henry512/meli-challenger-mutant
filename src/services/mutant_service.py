from abc import ABC, abstractmethod
from injector import inject
from src.domains import DNAEntity, DNAStatisticsDto
from src.repositories import IMutantRepository


class IMutantService(ABC):
    @abstractmethod
    def save_dna(self, dna: DNAEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_statistics(self) -> DNAStatisticsDto:
        raise NotImplementedError


class MutantService(IMutantService):
    @inject
    def __init__(self, repository: IMutantRepository):
        self._repository = repository
        
    def save_dna(self, dna: DNAEntity) -> None:
        self._repository.save_dna(dna)

    def get_statistics(self) -> DNAStatisticsDto:
        result = self._repository.get_statistics()
        return DNAStatisticsDto(
            count_human_dna=result["human"],
            count_mutant_dna=result["mutant"],
            ratio= result["ratio"]
        )
