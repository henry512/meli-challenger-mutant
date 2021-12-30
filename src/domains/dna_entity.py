from typing import List, TypedDict

from src.domains.dna_enum import DNAOriginEnum


class DNAEntity(TypedDict):
    sequence: List[str]
    origin: DNAOriginEnum
