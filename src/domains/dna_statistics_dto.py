from typing import TypedDict


class DNAStatisticsDto(TypedDict):
    count_mutant_dna: int
    count_human_dna: int
    ratio: float
